`sphinx-globaltoc`
==================

Have you ever wished you could keep a **single table of contents file** with
Sphinx, instead of embedding your document's structure in a collection of
page sourcefiles with the `toctree` directive? This extension is for you.

`sphinx-globaltoc` allows you to use a single YAML file to define a table of
contents for your entire site. This file should define all pages and sections
of those pages. Its basic structure is like this:

```yaml
path: myfirstpage.rst
sections:
  - path: mysecondpage.rst
    sections:
      - path: section1/a-subsection-page.md
        sections:
          - path: section1/section2/a-sub-subsection-page.md
  - path: mythirdpage.md
```

At a top level, we have the root of your documentation (here called
`myfirstpage.rst`). Normally, you'd need to call this `index.rst`, but this
extension will take the first `path:` item specified in your TOC file as
the site root.

If a page in your TOC file has a `sections:` key, then a `toctree` will be
added to that page with the `path:` of each section that you define.
These paths should be relative to the root of your content (AKA, the folder
where `myfirstpage.rst` is located).

For example, see the table of contents file of this documentation, shown below:

```{literalinclude} toc.yml
:language: yaml
```