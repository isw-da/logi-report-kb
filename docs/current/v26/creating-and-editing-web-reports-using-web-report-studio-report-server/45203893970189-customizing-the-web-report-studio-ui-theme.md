---
title: "Customizing the Web Report Studio UI Theme"
id: 45203893970189
section: "Creating and Editing Web Reports Using Web Report Studio Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203893970189-Customizing-the-Web-Report-Studio-UI-Theme
updated_at: 2026-04-30T14:07:34Z
source_host: logi-report-v26.insightsoftware.com
---
# 
            Customizing the Web Report Studio UI Theme

The web studio has added a light theme, so now web studio provides two UI themes: Light and Classic. You can choose either theme based on your personal preference.

For the newly added light theme, you can customize the Light by modifying CSS variable values. These variables allow you to adjust the appearance of the user interface, such as colors, fonts, and spacing, without changing the underlying theme structure. This makes it easy to personalize the look and feel of the application.

To customize a theme, you can edit the file %server_install_root%/public_html\webos\style\light\theme.css

find CSS variable defined in root

:root {

    ....

    --hover-background: #e8f4fc;

    --select-background: var(--brand-primary-50);

    --select-color: #000000;

    --icon-filter-invert: brightness(0) invert(1);

    --icon-invert-color: none;

    --main-toolbar-background: #f8f9fa;

    --main-toolbar-hover-background: var(--brand-primary-50);

    --main-toolbar-select-background: var(--brand-primary-100);

    --main-toolbar-color: #000000;

    --main-toolbar-border-color: #d9d9d9;

    --border-radius: 3px;

    --border-image: linear-gradient(to right, #ea62ae, #b564dd) 1;

    --main-background: #F3F3F3;

    --dialogtitle-background: var(--white);

    --dialogtitle-color: #1b1b1b;

    --dialogtitle-border-image: none;

    --dialogtitle-border-width: 0px;

    --dialogclient-background: var(--white);

    --dialogtitle-font-size: 25px;

    --dialogtitle-height: 38px;

    ....

}

CSS vairiables can be customized are listed here

| CSS variable name | Description |
| --- | --- |
| --input-background | Background color of input fields |
| --input-foreground | Text color of input fields |
| --button-primary-default | Default background color of primary buttons |
| --button-primary-hover | Background color of primary buttons on hover |
| --button-secondary-default | Default background color of secondary buttons |
| --button-secondary-hover | Background color of secondary buttons on hover |
| --button-link-default | Default color of link buttons |
| --button-link-hover | Color of link buttons on hover |
| --hover-background | Background color when hovering over elements |
| --select-background | Background color of select dropdowns |
| --select-color | Text color of select dropdowns |
| --icon-filter-invert | Icon color filter for inversion |
| --icon-invert-color | Icon invert color |
| --main-toolbar-background | Background color of the main toolbar |
| --main-toolbar-hover-background | Background color of the main toolbar on hover |
| --main-toolbar-select-background | Background color of the main toolbar when selected |
| --main-toolbar-color | Text color of the main toolbar |
| --main-toolbar-border-color | Border color of the main toolbar |
| --border-radius | Border radius for elements |
| --border-image | Border gradient style |
| --main-background | Main background color |
| --dialogtitle-background | Background color of dialog titles |
| --dialogtitle-color | Text color of dialog titles |
| --dialogtitle-border-image | Border style of dialog titles |
| --dialogtitle-border-width | Border width of dialog titles |
| --dialogclient-background | Background color of dialog content area |
| --dialogtitle-font-size | Font size of dialog titles |
| --dialogtitle-height | Height of dialog titles |

After changing the variables to the values you want, save the theme.css file, and then run make.bat/make.sh in the <install_root>\public_html\bin directory to make the changes take effect.
The above variables can affect the overall UI content of web studio. If you need to make individual adjustments to the CSS in a certain area, you can refer to this Customizing the Web Report Studio UI
