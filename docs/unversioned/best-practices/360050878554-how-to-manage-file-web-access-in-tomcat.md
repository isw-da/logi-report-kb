---
title: "How to Manage File Web Access in Tomcat"
id: 360050878554
section: "Best Practices"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360050878554-How-to-Manage-File-Web-Access-in-Tomcat
updated_at: 2020-08-14T19:31:48Z
---

# How to Manage File Web Access in Tomcat

### Question:

What mechanisms are available to restrict access to source file browsing of .jspf files by URL?

See below screenshot for details:

![logireportimg1.PNG](https://devnet.logianalytics.com/hc/article_attachments/360078872634/logireportimg1.PNG)

Note: **JSPF***file is a Java Server Page Fragment. A JSP fragment with a***.jspf***extension, embedded with the JSP include directive, and compiled together with the parent page.*

### Solution:

Since Logi Report (Jreport) was originally designed to work as a standalone server, all javascript, css, image, html, jsp, and, jspf files are located under the '**public\_html**' folder, which is the UI entry point of standalone server.

Since the .css, .js, .jspf files include a directive relative path that is fixed, all the files are placed under '**public\_html**' folder to the root directory of '**jreport.war**' when integrated with Tomcat (web server) as a WAR application.

While files with other extensions (example:  js, css) are not directly accessible by URL, since '**\*.jspf**' is a plain text file (file also contains partial jsp code), it is possible to view it in browser directly once the user knows the exactly URL path.  
  
To restrict '**.jspf**' file direct access, following solution can be used in web server ( ***Note:** following solution assumes the underlying web server as 'Tomcat'*):

Add following security-constraint in **jreport.war web.xml**: 

```
 <security-constraint>  
        <web-resource-collection>  
            <web-resource-name>jreport</web-resource-name>  
            <url-pattern>*.jspf</url-pattern>  
        </web-resource-collection>  
        <auth-constraint/>  
 </security-constraint> 
```

Add a customized error page in 'web.xml' as below to display

```
 <error-page>  
    <error-code>403</error-code>  
    <location>/error.html</location>  
 </error-page>
```

![logireportimg2.PNG](https://devnet.logianalytics.com/hc/article_attachments/360078880614/logireportimg2.PNG)
