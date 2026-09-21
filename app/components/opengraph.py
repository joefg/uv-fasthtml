from fasthtml.common import Meta

def Og(tag, content): return Meta(property=f"og:{tag}", content=content)

# Required
def OgTitle(content): return Og('title', content)
def OgType(content): return Og('type', content)
def OgImage(content): return Og('image', content)
def OgUrl(content): return Og('url', content)

# Optional
def OgAudio(content): return Og('audio', content)
def OgDescription(content): return Og('description', content)
def OgDeterminer(content): return Og('determiner', content)
def OgLocale(content): return Og('locale', content)
def OgLocaleAlternate(content): return Og('locale:alternatte', content)
def OGSiteName(content): return Og('site_name', content)

# Structured - image
def OgImageURL(content): return Og('image:url', content)
def OgImageSecureURL(content): return Og('image:secure_url', content)
def OgImageType(content): return Og('image:type', content)
def OgImageWidth(content): return Og('image:width', content)
def OgImageHeight(content): return Og('image:height', content)
def OgImageAlt(content): return Og('image:alt', content)

# Structured - video
def OgVideoURL(content): return Og('video:url', content)
def OgVideoSecureURL(content): return Og('video:secure_url', content)
def OgVideoType(content): return Og('video:type', content)
def OgVideoWidth(content): return Og('video:width', content)
def OgVideoHeight(content): return Og('video:height', content)
def OgVideoAlt(content): return Og('video:alt', content)

# Structured - audio
def OgSoundURL(content): return Og('sound:url', content)
def OgSoundSecureURL(content): return Og('sound:secure_url', content)
def OgSoundType(content): return Og('sound:type', content)
