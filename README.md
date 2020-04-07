[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/pywrm/pywrm) 

# pywrm
Python widget relational model


### Proposed file structure
* PyWRM (Repo)
  * pywrm
    * app (aka fast API)
    * modules
      * chappie_cookie_company.py
      * hello_world.py
      * widget_demo.py
    * pywrm_widgets (uses external_widgets)
      * rich_text.py (top level class for ace_rich_text.py)
      * toolbar.py (top level class for dhx_toolbar.py and w2ui_toobar.py) (basically ORM like object)
    * external_widgets
      * abc (abstract base class for rendered_widgets)
        * abc_toolbar.py
        * abc_rich_text.py
      * ace
        * raw_widgets (generated from widget_parser)
        * ace_rich_text.py
      * dhx
        * raw_widgets (generated from widget_parser)
        * dhx_toolbar.py
        * dhx_rich_text.py
      * w2ui
        * raw_widgets (generated from widget_parser)
        * w2ui_toobar.py
    * static
      * css
      * templates
        * main.html (creates main widget pane, include js libs)
      * jscript
        * pwrm.js
    * main.py
  * extra
    * w2ui
  * scripts
    * widget_parser (writes to raw_widgets for each widgetset)
      * parsers
        * ace_parser_v?.py
        * dhx_parser_v?.py
        * w2ui_parser_v?.py
      * widget_parser.py
  * examples
    * hello_world
    * chappie_cookie_company
    * widget_demo
    * Dockerfile
    * EXAMPLES.md (If this doesn't render, put README.md)
  * README.md
  * CHANGELOG.md
  * LICENSE
  * requirements.txt
  * MANIFEST.in
  * setup.py (only support python 3.7 and up)
  * setup.cfg
  * unittesting
