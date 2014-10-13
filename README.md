# NTUOSC Site

Landing page & blog for National Taiwan University Open Source Community. This repository holds the ground-up site source.

## Prerequisites

This website is generated using [Pelican](http://getpelican.com). To install all the Python dependencies, simply run the following command:

    [sudo] pip install pelican Markdown Fabric

If you're tweaking the site stylesheet, make sure to install [Bower](http://bower.io) and [Sass](http://sass-lang.com):

    [sudo] npm install -g bower
    [sudo] gem install sass

And run

    bower install

to fetch all the required frontend components.


## To build

[Fabric](http://www.fabfile.org) is used to do all the automation works. To list available commands, try:

    fab --list

And run either `fab build` or `fab serve` to generate pages or run the site locally.

`fab sass` compiles SCSS stylesheets into compressed CSS. Here are some possible usages:

    fab sass
    fab sass:watch
    fab sass:compile,force build serve
    fab sass:,,style=expanded,sourcemap=auto

See SASS and Fabric documentation for more options.

## Deployment

Before publishing the site, make sure you've set up correct `git` remote branches already:

    git remote add github https://github.com/NTUOSC/ntuosc.github.io.git

Note that weʻre deploying to root GitHub Pages repository. To change the behavior, modify `fabfile.py` in the project directory as your wish.

When you‘re all set, run the following command,

    fab github

to publish the site on GitHub Pages.


## License

Except noted individually, the site itself is licensed under [Creative Commons Attribution-ShareAlike 4.0](http://creativecommons.org/licenses/by-sa/4.0/). Hope you could make something useful out of our materials.

Authored by [Poren Chiang](http://poren.tw) 2014.
