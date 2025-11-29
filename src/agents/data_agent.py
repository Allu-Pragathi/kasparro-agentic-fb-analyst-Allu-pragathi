import pandas as pd
from pathlib import Path
class DataAgent:
    def __init__(self, config):
        self.config = config
        self.path = config.get('data_csv') if config else '/mnt/data/synthetic_fb_ads_undergarments.csv'
    def _load(self):
        df = pd.read_csv(self.path, parse_dates=['date'])
        return df
    def run(self):
        df = self._load()
        # create basic summaries
        summary = {}
        df['roas'] = df.get('roas', df.get('revenue',0) / df.get('spend',1).replace(0,1))
        # last 7 days vs previous 7 days
        max_date = df['date'].max()
        last7 = df[df['date'] > (max_date - pd.Timedelta(days=7))]
        prev7 = df[(df['date'] <= (max_date - pd.Timedelta(days=7))) & (df['date'] > (max_date - pd.Timedelta(days=14)))]
        def agg(d):
            return {
                'spend': d['spend'].sum(),
                'impressions': d['impressions'].sum(),
                'clicks': d['clicks'].sum(),
                'ctr': (d['clicks'].sum() / max(d['impressions'].sum(),1)),
                'purchases': d.get('purchases', pd.Series([])).sum(),
                'revenue': d.get('revenue', pd.Series([])).sum(),
                'roas': (d.get('revenue', pd.Series([0])).sum() / max(d['spend'].sum(),1))
            }
        summary['last7'] = agg(last7)
        summary['prev7'] = agg(prev7)
        # CTR by campaign
        ctr_by_campaign = df.groupby('campaign_name').apply(lambda g: (g['clicks'].sum() / max(g['impressions'].sum(),1))).to_dict()
        summary['ctr_by_campaign'] = ctr_by_campaign
        # low CTR campaigns
        ctr_low_thresh = self.config.get('ctr_low_threshold', 0.012) if self.config else 0.012
        summary['low_ctr_campaigns'] = [c for c,v in ctr_by_campaign.items() if v < ctr_low_thresh]
        # sample creative messages per campaign
        creative_samples = df.groupby('campaign_name')['creative_message'].agg(lambda s: s.dropna().unique()[:3].tolist()).to_dict()
        summary['creative_samples'] = creative_samples
        summary['max_date'] = max_date.strftime('%Y-%m-%d')
        return summary
