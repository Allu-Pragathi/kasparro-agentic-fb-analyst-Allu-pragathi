import random
class CreativeGenerator:
    def __init__(self):
        random.seed(42)
    def run(self, data_summary):
        out = {}
        low = data_summary.get('low_ctr_campaigns', [])
        creative_samples = data_summary.get('creative_samples', {})
        for c in low:
            samples = creative_samples.get(c, [])
            # naive generation: vary existing samples
            headlines = []
            primary_texts = []
            ctas = ["Shop Now", "Try It Today", "Learn More"]
            for i in range(3):
                base = samples[i] if i < len(samples) else "Our product designed for comfort."
                headlines.append(f"{base.split('.')[0][:60]} — Now Better")
                primary_texts.append((base + " Limited time offer.").strip()[:140])
            out[c] = {"headlines": headlines, "primary_texts": primary_texts, "ctas": ctas}
        return out
