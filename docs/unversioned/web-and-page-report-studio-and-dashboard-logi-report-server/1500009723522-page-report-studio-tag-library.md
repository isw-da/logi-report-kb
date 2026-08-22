---
title: "Page Report Studio Tag Library"
id: 1500009723522
section: "Web and Page Report Studio and Dashboard Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009723522-Page-Report-Studio-Tag-Library
updated_at: 2021-07-25T07:18:51Z
---

# Page Report Studio Tag Library

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009723502-Advanced-Exporting-with-JSPs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744981-JDashboard)

# Page Report Studio Tag Library

Page Report Studio provides its tag library, which includes custom tags such as mainpage, head, toc and report. These custom tags can be used to componentize JSP pages, increasing productivity and encapsulating recurring tasks so that they can be reused across more than one application.

For technique topics on the JSP tag library, references can be found in JSP online documentation on the Sun Microsystems website <http://www.sun.com>.

Page Report Studio tags are classified as follows:

* [Embedded Tags](#Embedded)
* [Component Tags](#Component)
* [Action Tags](#Action)

Before you can use the Page Report Studio tag library in Logi Report Server, you should first copy the file Jinfonet\_DHTML\_taglib.tld in `<install_root>\public_html\dhtmljsp` to the folder where your JSP pages are located.

And if you want to use the Page Report Studio tag library in any web server, you should first:

1. Add JRWebDesign.jar in `<install_root>\lib` to the war file you want to publish to the web server.
2. Add Jinfonet\_DHTML\_taglib.tld in `<install_root>\public_html\dhtmljsp` to the war file in which your JSP pages reside, or alternatively, you can use web.xml to specify a path. For example,

   ```
   <taglib>  
   <taglib-uri>Jinfonet_DHTML_taglib</taglib-uri>  
   <taglib-location>/WEB-INF/Jinfonet_DHTML_taglib.tld</taglib-location>  
   </taglib>
   ```

## Embedded Tags

**dhtml**

The dhtml tag is a container for the other tags, and it checks user information, runs a report, and imports resources for the other tags. All tags to be used should be included in this tag. It contains the following attributes:

| Attribute | Description |
| --- | --- |
| id - string | Specifies the ID of the tag. |
| tagsetid - string | Specifies the ID of the tag set. This attribute is required. |
| user - string | The user name for logging in Logi Report Server. |
| password - string | The user password for logging in Logi Report Server. |
| report - string | The name of the report the user wants to run. This attribute is required. |
| catalog - string | The name of the catalog for the report. This attribute is required. |
| report\_path - string | The path of the report. |
| report\_params - string | All parameters (name/value pair) that are required for running the report, and the parameters are separated by & character. |
| catalog \_version - integer | The catalog version. Default value is 1. |

**mainpage**

The mainpage tag displays the Page Report Studio page in an IFrame. It contains the following attributes:

| Attribute | Description |
| --- | --- |
| width=length | The width of the frame. It can be a relative or absolute value, for example, 70% or 1000px. |
| height=length | The height of the frame. It can be a relative or absolute value, for example, 70% or 1000px. |
| top=length | The top position of the frame, measured in pixels. |
| left=length | The left position of the frame, measured in pixels. |
| align=[top/middle/|bottom/left/right] | Specifies where the frame appears in the web browser window.  * top - Aligns the frame to the top of the web browser window. * middle - Aligns the frame to the middle of the web browser window. * bottom - Aligns the frame to the bottom of the web browser window. * left - Aligns the frame to the left of the web browser window. * right - Aligns the frame to the right of the web browser window. |
| frameborder=[1/0] | Sets or retrieves whether to display the frame border. Use 1 to show the frame border, or 0 to hide it. |
| scrolling=[yes/no/auto] | Sets or retrieves whether the frame can be scrolled.  * auto - Default. The web browser determines whether scrollbars are necessary. * yes - The frame can be scrolled. * no - The frame cannot be scrolled. |
| id - string | Specifies the ID of the frame. |
| name - string | Specifies the frame name. |
| position=[static/absolute/relative] | Sets or retrieves the type of positioning used for the object.  * static - Default. Object has no special positioning; it follows the layout rules of HTML. * absolute - Object is positioned relative to parent element's position—or to the body object if its parent element is not positioned—using the top and left properties. * relative - Object is positioned according to the normal flow, and then offset by the top and left properties. |
| controls=[userInfoBar|rptSetBar|toolbar|  Toc|Dso|report|toolbox|linkbar|all] | All components that the user wants to display. The user can set any one or more of them, or use all to display all the components. |

## Component Tags

**toc**

The toc tag is for displaying the TOC Browser.

**toolbar**

The toolbar tag is for displaying the toolbar.

**resview**

The resview tag is for displaying the Resource View panel.

**toolbox**

The toolbox tag is for displaying the Toolbox.

**button**

The button tag is for displaying buttons which match toolbar buttons but they can be placed anywhere in Page Report Studio.

| Attribute | Description |
| --- | --- |
| buttonid | Identifies the specific button. You can obtain a constant Java class jet.web.dhtml.DHTMLConstant from the package JRWebDesign.jar located at `<install_root>\lib`. In this class, those constants with a prefix "TOOLBAR\_" and of int data type represent the buttonid, and you can then know the buttonid according to the constant name. For example, `<jinfonet:button buttonid="<%=String.valueOf(DHTMLConstant.TOOLBAR_NEW)%>">` will display the New button. This attribute is required. |

**toolboxbutton**

The toolboxbutton tag is for displaying buttons which match Toolbox buttons but they can be placed anywhere in Page Report Studio.

| Attribute | Description |
| --- | --- |
| component\_type | Identifies the specific button. These constants are available for component\_type: "Label", "Image", "Banded Object", "Table", "Crosstab", and "Chart". For example, `<jinfonet:toolboxbutton component_type="Banded Object"/>` will display the Banded Object button. This attribute is required. |

**report**

The report tag is for Page Report Studio browser.

| Attribute | Description |
| --- | --- |
| width=length | The width of the report browser, measured in pixels. Use -1 to set it to 100% of Internet Explorer window's width. In other web browsers, -1 means 650 pixels. |
| height=length | The height of the report browser, measured in pixels. Use -1 to set it to 100% of Internet Explorer window's height. In other web browsers, -1 means 600 pixels. This attribute is required. |
| top=length | The top position of the report browser, measured in pixels. |
| left=length | The left position of the report browser, measured in pixels. |
| id | Specifies the ID of the tag. |
| class\_name | Retrieves the class of the object. |
| style | Sets a style for the object. |
| controls=[rptSetBar|linkbar|all] | Specifies whether to display the components. The user can set any one or more of them, or use all to display all the components. |

## Action Tags

**sortform**

The sortform tag will generate a form for sorting the data. It contains the following attributes:

| Attribute | Description |
| --- | --- |
| id - string | Specifies the ID of the tag. This attribute is required. |
| method - string | Sets or retrieves how to send the form data to the server.  * get **-**  Appends the arguments to the Form Action URL and opens it as if it were an anchor. * post **-**  Sends the data through an HTTP post transaction. |
| forward - string | Specifies the page to redirect. If it starts with /, the root path refers to `<install_root>\public_html`; if with no /, the root refers to `<install_root>\public_html\dhtmljsp`. |
| target - string | Sets the window or frame at which to target content. |
| applyto - string | Specifies the instance name of the component on which the sorting will be based. This attribute is required. |

**filterform**

The filterform tag will generate a form for filtering the data. It contains the following attributes:

| Attribute | Description |
| --- | --- |
| id - string | Specifies the ID of the tag. This attribute is required. |
| method - string | Sets or retrieves how to send the form data to the server.  * get **-**  Appends the arguments to the Form Action URL and opens it as if it were an anchor. * post **-** Sends the data through an HTTP post transaction. |
| forward - string | Specifies the page to redirect. If it starts with /, the root path refers to `<install_root>\public_html`; if with no /, the root refers to `<install_root>\public_html\dhtmljsp`. |
| target - string | Sets the window or frame at which to target content. |
| applyto - string | Specifies the instance name of the component on which the sorting will be based. This attribute is required. |

**column**

The column tag will generate a list to provide sorting manners for the sortform tag or field values for the filterform tag. It contains the following attributes:

| Attribute | Description |
| --- | --- |
| id - string | Specifies the ID of the tag. This attribute is required. |
| bind\_column - string | Specifies the column by which to sort or filter. This attribute is required. |
| logic - string | Specifies the relationship between the filter criterion and the next one. Its value can be "AND" or "OR". Only for filterform. |
| maxsize - integer | Specifies the maximum number of the items in the list, only for filterform. |
| parent\_id - string | Specifies the ID of the sortform or filterform tag which includes the column tag. This attribute is required. |
| class\_name - string | Specifies the class name. |
| style - string | Specifies the style of the list. |
| width - string | Specifies the width of the list. |
| top - integer | Specifies the top position of the list. |
| left - integer | Specifies the left position of the list. |

**Reference:** For examples about the tags, refer to the file ExampleCodeForTags.html in `<install_root>\help\samples\URLSamples`, where some sample code for different tags is provided. To test the examples, save the code to tagtest.jsp and then put it in `<install_root>\public_html\dhtmljsp`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009723502-Advanced-Exporting-with-JSPs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744981-JDashboard)
