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

Icons are namespaced as `extraicons--` to avoid clashing with existing Wagtail icons. You can add the extra icons to 
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

## License

This project is licensed under the BSD License - see the [LICENSE.md](LICENSE.md) file for details
