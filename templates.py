#!/usr/local/bin/python3


pic_link_template = """
<div class="pic-container">
    <a href="{PIC_HTMLS_DIR}/{pic_html_filename}">
        <div class="{thumbnail_name}">
        </div>
    </a>
</div>
"""


pic_html_template = """
<html>
  <head>
    <meta charset="utf-8"/>
    <link rel="stylesheet" href="../stylesheet.css"/>
  </head>
  <body>
    <div style="width: 100%;">
      <div class="menu-box">
      <div class="menu-options">
        <ul>
          <li><a class="navigation-text" href="{prev_pic_html_filename}"> Previous </a></li>
          <li><a class="navigation-text" href="../index.html"> Home </a></li>
          <li><a class="navigation-text" href="{next_pic_html_filename}"> Next </a></li>
        </ul>
      </div>
      </div>
      <div class="gallery-box"><img class="pic" src="{pic_path}">
      </div>
    </div>
  </body>
</html>
"""


thumbnail_css_template = """
.{thumbnail_name} {{
  width: 300px;
  height: 300px;
  background-image: url('{thumbnail_path}');
  background-size: 100%;
  background-repeat: no-repeat;
  background-position: center center;
  image-orientation: from-image;
}}
"""
