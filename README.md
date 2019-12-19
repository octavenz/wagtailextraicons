# Wagtail Extra Icons

Add extra icons to your Wagtail project.

## Install

```
pip install wagtailextraicons
```

Then add `wagtailextraicons` to your installed apps:

```
INSTALLED_APPS = [
    ...
    'wagtailextraicons'
]
```

## Usage

The full list of icons is available at [docs/icons.md](https://github.com/octavenz/wagtailextraicons/blob/master/docs/icons.md). 
All icons are namespaced as `extraicons--` to avoid clashing with existing Wagtail icons. You can add the extra icons to 
your StreamField blocks like any other:

```python
content = StreamField([
    (
        'paragraph',
        blocks.RichTextBlock(icon='extraicons--paragraph')
    ),
])
```

You can also add the extra icons to your own custom `StructBlock` classes:

```python
class PersonBlock(blocks.StructBlock):
    person = SnippetChooserBlock('app.Person')
    text = blocks.RichTextBlock()

    class Meta:
        icon = 'extraicons--person'
```

Reference the [Wagtail docs](http://docs.wagtail.io/en/latest/topics/streamfield.html) for all the ways to include icons.  

## Authors

* **Sam Costigan** [Octave](https://github.com/octavenz)

## Contributing

The icon fonts are compiled from the list of SVG files in [static_src/wagtailextraicons/extraicons](https://github.com/octavenz/wagtailextraicons/tree/master/wagtailextraicons/static_src/wagtailextraicons/extraicons).
This makes it very easy to add new icons. All that's needed is an appropriate SVG file, so pull requests with new icons
are always welcome. There are a few constraints on the icons however:

* The icons must fit within their view box. Icons which don't will cause the fonts view box to have negative values,
which results in invalid .ttf and .woff files.
* Try to avoid using strokes, rects, etc. in your SVG. Some of these *may* work, but plain paths will *always* work, 
so prefer paths where possible.
* Don't set colours on your SVG.

Code pull requests are also welcome.

## License

This project is licensed under the BSD License - see the [LICENSE.md](LICENSE.md) file for details
