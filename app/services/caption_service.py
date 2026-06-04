from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration
)

from PIL import Image

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)


def generate_caption(image_path: str):

    image = Image.open(image_path).convert("RGB")

    inputs = processor(
        image,
        return_tensors="pt"
    )

    output = model.generate(
        **inputs,
        max_new_tokens=15
    )

    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    stop_words = {
        "a", "an", "the", "is", "are",
        "of", "on", "in", "at", "with",
        "and", "to", "for", "by", "from"
    }

    hashtags = []

    words = caption.lower().split()

    for word in words:

        clean_word = "".join(
            c for c in word
            if c.isalnum()
        )

        if (
            len(clean_word) > 3
            and clean_word not in stop_words
        ):
            hashtags.append(
                "#" + clean_word.capitalize()
            )

    hashtags = list(
        dict.fromkeys(hashtags)
    )[:5]

    return {
        "caption": caption,
        "hashtags": hashtags
    }