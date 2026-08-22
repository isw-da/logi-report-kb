---
title: "Accessing Report Server via a Web Browser"
id: 28891701972109
section: "Starting, Accessing, and Shutting Down Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891701972109-Accessing-Report-Server-via-a-Web-Browser
updated_at: 2026-02-26T02:14:18Z
source_host: docs-report.zendesk.com
---
# 
Accessing Report Server via a Web Browser 

You can access Report Server through a web browser such as Firefox and Google Chrome. This topic describes how you can sign in to the Server Console locally or via URL, search for resources and properties on the Server Console, and sign out.

The Server Console provides a unified UI for normal users and administrators (users who have the "administrators" role, also referred to as administrators) to access and manage server resources depending on authorization. Normal users can perform report related tasks such as running and creating reports and dashboards, starting visual analysis, and customizing their own server preferences. Administrators can also perform administrative tasks such as managing security and databases, configuring the server, and setting up a Cluster.

 Before accessing the Server Console, you should have started Server first.

This topic contains the following sections:

- Signing in to the Server Console Locally
                

- Signing in to the Server Console by URL                

- Additional Channel for Administrators to Sign In                

- Searching for Resources on the Server Console                

- Signing out of Report Server                

- Theme Customization          

## 
Signing in to the Server Console Locally 

To access the  Server Console from the same machine on which you installed Report Server, take the following steps:

- 
Start Server.

- Server displays a welcome page automatically in your default web browser. Provide your username and password as assigned by your administrator. When Server enables Organization and your user account belongs to an organization, you need to also specify the correct organization name. The default organization name System means that you do not belong to any organizations. Select Remember Me if you want Server to remember your information.

Username for signing in to the Server Console should be case sensitive by default. You can change this by clearing the Case-Sensitive Login User Name option in the server profile, if you are an administrator.

- Select LOGIN. Server displays the home page of the Server Console which can be the Start Page, the Console page, or a dashboard depending on the Home Page setting in the server profile.
				The Start Page is the default home page of the Server Console. It provides quick entries to some key functions. Choose a topic to start your work on the server.

| Option | Description |
| --- | --- |
| How To |  |
| Feature Guide | Select if you want to read Report Feature Guide about Report's main features. |
| Demo | Select if you want to view dashboards and reports demos. |
| Tutorial | Select if you want to read Report Tutorial. |
| Create |  |
| Dashboard | Select if you want to create a dashboard. |
| Web Report | Select if you want to create a web report. |
| Page Report | Select if you want to create a page report. |
| Open |  |
| My Folder | Select if you want to open the My Reports folder on the Server Console. |
| Public Folder | Select if you want to open the Public Reports folder on the Server Console. |
| Manage |  |
| My Profile | Select if you want to open the Server Console > My Profile > Customize Server Preferences page for configuring the server profile settings of your own. |
| Schedule | Select if you want to schedule a task to run a report. |
| Administration | Select if you want to open the Server Console > Administration > Configuration > Advanced page for managing the server advanced resources. Available to administrators only. |
| Others |  |
| Username | The name of the current user who signed in. |
|  | Select if you want to sign out of the server. |
| User's Guide | Select if you want to read Report Server Guide. |
| Report Home Page | Select if you want to go to the Logi Analytics home page. |
| Contact Support | Select if you want to go to the Logi Analytics support portal. |
| Do not show this page at start up | Select if you want to access the Server Console instead of Start Page as the home page after Server starts next time. You can display Start Page by selecting the Start Page icon on the system toolbar of the Server Console. |

## 
Signing in to the Server Console by URL

Sometimes you may have closed the Start Page or the Server Console while the local server remains started, or you are accessing the Server Console from a remote computer, you can access it by URL:

- Open a web browser and set the URL to http://IP_or_HostName_or_DomainName:port (by default the port for accessing the Server Console is 8888).
      If you do not know the IP address of the machine on which the server runs, and it is the same machine where you are going to sign in, you can use localhost instead of the IP address. You can also open a console window such as telnet on the server computer and type hostname to get the name of the host.

- Server displays the welcome page. Type your username and password as assigned by your administrator.

- Select LOGIN. Server displays the Server home page.

 If you are accessing Report Server from another computer or port in a different domain, you need to add the following lines to the responseHeaders.properties file in the <server_install_root>\bin:

access-control-allow-origin:   *
vary: origin

## 
Additional Channel for Administrators to Sign In

Report Server provides a special channel that automatically creates an extra user session for management purposes if the license limit of the maximum number of concurrent users has been reached. You cannot use the extra user session to run reports or submit schedule tasks. You can only perform management operations as an administrator. If your Report Server license has a bounded limit to the maximum number of concurrent users, this feature will take effect. 

Server creates only one extra valid user session within this special channel at any time. If an extra user session already exists and is still valid, Server displays a confirmation page asking you whether to close the existing extra user session. Only when you close the existing user session can Report Server start a new user session for you to perform management operations. Otherwise, you cannot sign in to Report Server.

## 
Searching for Resources on the Server Console

On the Server Console, you can make use of the Global Search feature to search for the resources and properties you need. You can perform global search  anywhere on the Server Console to search among the following:

- 
Report resources such as reports, catalogs, dashboards, library components, and folders in the server resource tree.

- 
Scheduled and background tasks.
            

- Properties in the My Profile > Customize Server Preferences and Customize Profile pages.

- 
Users, groups, roles, and organizations  in the Administration > Security page that is available to administrators only.

To use global search, select the Global Search button  on the system toolbar. Server displays the following search page.

In the search box, type the text you want to search for and Server lists the resources that contain the matched text (for the My Profile page, Server lists the properties whose key values contain the matched text). In the search result list, select a property and Server displays the page where the property is and highlights the matched text. When there are more than 10 results, you can select More at the end to show all the other results. To cancel the search operation, clear the text in the search box or select .

## 
Signing out of Report Server

To sign out from the Start Page, select the  icon at the upper right corner. 

To sign out from the Server Console, select the User icon  at the upper right corner and then select Logout from the drop-down menu.

## 
Theme Customization

The server provides two UI themes: Light and Classic. You can choose either theme based on your personal preference.

In addition, you can customize the Light or Classic theme by modifying CSS variable values.

These variables allow you to adjust the appearance of the user interface, such as colors, fonts, and spacing, without changing the underlying theme structure. This makes it easy to personalize the look and feel of the application.

To customize a theme, you can edit the file %server_install_root%/public_html/javascript/common.js.

find js object Themes defined in common.js.

const Themes = {

  light: {

    '--default-color': 'var(--Brand-Primary-500)',

    ...

  },

  default: {  // classic theme

    '--default-color': 'transparent',

    ...

  }

};

Values of CSS variable of various theme are defined in js object Themes.light and Themes.default, you can modify CSS variable values to apply your preferred value.

Values of CSS variable defined in Themes.light takes effect when Light theme is selected, and defined in Themes.default takes effect when Classic theme is selected.

CSS vairiables can be customized are listed here:

| CSS variable name | description |
| --- | --- |
| --default-color | default color (brand color) |
| --launchpad-deepblue | background color of panes in “How To” column on launchpad page |
| --launchpad-deepblue-over | background color of pane when mouse over it in “How To” column on launchpad page |
| --launchpad-deepblue-click | background color of pane when click it in “How To” column on launchpad page |
| --launchpad-blue | background color of panes in “Create” column on launchpad page |
| --launchpad-blue-over | background color of pane when mouse over it in “Create” column on launchpad page |
| --launchpad-blue-click | background color of pane when click it in “Create” column on launchpad page |
| --launchpad-green | background color of panes in “Open” column on launchpad page |
| --launchpad-green-over | background color of pane when mouse over it in “Open” column on launchpad page |
| --launchpad-green-click | background color of pane when click it in “Open” column on launchpad page |
| --launchpad-oringe | background color of panes in “Manage” column on launchpad page |
| --launchpad-oringe-over | background color of pane when mouse over it in “Manage” column on launchpad page |
| --launchpad-oringe-click | background color of pane when click it in “Manage” column on launchpad page |
| --launchpad-border-radius | pane’s border radius on launchpad page |
| --topbar-hover-background-color | background color of menu when mouse hover |
| --topbar-background-color | top banner background color |
| --topbar-color | color of menu text on top banner |
| --topbar-hover-color | color of menu text on top banner when mouse over |
| --topbar-on-background-color | background color of menu on top banner when menu is selected |
| --topbar-underline-color | underline color of selected menu on top banner |
| --topbar-underline-height | underline height of selected menu on top banner |
| --topbar-underline-width | underline width of selected menu on top banner |
| --topbar-gradient-line | gradient color line at bottom of top banner |
| --image-filter | image filter to inverse image color of icons at top-right corner |
| --border-radius | default border radius |
| --input-border-radius | border radius of input and select, textarea |
| --font-face | font face |
| --font-face-light | font face light |
| --font-faces | font faces |
| --highlight-icon-color | color of highlighted icon of page mode toggle icons |
| --hover-color | background color when mouse hover a item |
| --selected-color | background color when a item is selected |
| --checkbox-background-color | background color in checkbox |
| --checkbox-checkmark-color | checkmark color in checkbox |
| -checkbox-checkmark-thick | checkmark thickness in checkbox |
| --checkbox-checked-border-color | border color when checkbox is checked |
| --checkbox-hover-color | checkbox color when mouse hover it |
| --checkbox-disable-checkmark-color | checkmark color when checkbox is disabled |
| --checkbox-disable-background-color | background color when checkbox is disabled |
| --checkbox-border-radius | border radius of checkbox |
| --radio-color | color of radio button |
| --button-border-radius | border radius of button |
| --button2-border-radius | border radius of button style 2 |
| --button-background | button background color |
| --button-default-background | default button background color |
| --button-default-color | default button text color |
| --button-hover-background | button background color when mouse hover |
| --button-default-hover-background | default button background color when mouse hover |
| --button-panel2-background | background color of button’s container on few pages |
| --link-color | link text color |
| --loginform-color | “LOGIN” button background color on login form |
| --loginform-input-border-radius | input border radius on login form |
| --loginform-button-border-radius | “LOGIN” button border radius on login form |
| --dialog-back-padding | padding around panel on most page |
| --dialog-background-color | background color of the panel |
| --dialog-border-radius | panel border radius |
| --dialog-body-border-radius | content area border radius |
| --tab-background-color | tabs background color |
| --tab-border-radius | tab border radius |
| --tab-spacing-height | vertical space between tabs (if necessary) |
| --tab-padding-top | top padding of tab (if necessary) |
| --tab-padding-width | horizontal space before/after tab |
| --tab-level2-display | value of css property “display” for the deepest level tab |
| --tab-level2-margin-left | margin before the deepest level tab |
| --tab-level2-background-color | the deepest level tab background color |
| --tab-level2-table-border | border of the deepest level tab |
| --sdialog-body-padding | content area padding on some pages |
| --row-odd-background | odd row background color on resource list page |
| --row-even-background | even row background color on resource list page |
| --floaticon-odd-background | background color of float icon in odd row |
