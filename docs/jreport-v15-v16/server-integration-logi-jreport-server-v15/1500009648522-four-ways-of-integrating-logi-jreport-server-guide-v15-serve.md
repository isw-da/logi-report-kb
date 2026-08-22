---
title: "Four Ways of Integrating Logi JReport Server Guide v15 Server"
id: 1500009648522
section: "Server Integration Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009648522-Four-Ways-of-Integrating-Logi-JReport-Server-Guide-v15-Server
updated_at: 2021-07-24T20:54:10Z
---

# Four Ways of Integrating Logi JReport Server Guide v15 Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673221-Specifying-Reporthome-for-Logi-JReport-Server-Guide-v15-Server-in-a-Java-EE-Environment)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673041-Deploying-Logi-JReport-Server-Guide-v15-Server-to-a-Java-Application-Server)

# Four Ways of Integrating Logi JReport Server

To integrate Logi JReport Server with your application server, you can either create a Logi JReport Server WAR/EAR, or create your WAR/EAR and embed a self-contained Logi JReport Server inside it. For how to create a Logi JReport Server WAR/EAR, see [Building a WAR/EAR file to Include a Self-contained Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009648502-Building-a-WAR-EAR-file-to-Include-a-Self-contained-Logi-JReport-Server-Guide-v15-Server).

Below is a list of the sections covered in this topic:

* [Integrating by Building a Logi JReport Server WAR](#Way1)
* [Integrating by Building a Logi JReport Server EAR](#Way2)
* [Integrating by Building a User WAR and Embedding a Self-Contained Logi JReport Server](#Way3)
* [Integrating by Building a User EAR and Embedding a Self-Contained Logi JReport Server](#Way4)

## Integrating by Building a Logi JReport Server WAR

The self-contained Logi JReport Server can be deployed as a single WAR file.

For example, you can create a Logi JReport Server WAR file named Logi JReport.war and the structure of the Logi JReport Server WAR is as follows:

**Logi JReport.war**

WEB-INF/

web.xml

lib/ -- This folder contains all resources in the Logi JReport Server library.

admin/ -- This folder contains JSP files for the Logi JReport Administration page.

jinfonet/ -- This folder contains JSP files for the Logi JReport Console page.

dhtmljsp/ --This folder contains JSP files for viewing page reports.

The following is a sample of the content in the web.xml file of the Logi JReport Server WAR:

|  |
| --- |
| ``` <?xml version="1.0" encoding="ISO-8859-1"?>  <!DOCTYPE web-app PUBLIC "-//Sun Microsystems,  Inc.//DTD Web Application 2.3//EN"  "http://java.sun.com/dtd/web-app_2_3.dtd">  <web-app>     <listener>          <listener-class>jet.server.servlets.JRServerContextListener</listener-class>     </listener>     <servlet>         <servlet-name>jrserver</servlet-name>         <servlet-class>jet.server.servlets.JRServlet</servlet-class>     </servlet>     <servlet>         <servlet-name>sendfile</servlet-name>         <servlet-class>jet.server.servlets.SendFileServlet</servlet-class>     </servlet>     <servlet>         <servlet-name>dhtml</servlet-name>         <servlet-class>jet.web.dhtml.DHTMLlet</servlet-class>     </servlet>     <servlet>         <servlet-name>help</servlet-name>         <servlet-class>jet.web.dhtml.JHelplet</servlet-class>      </servlet>     <servlet-mapping>         <servlet-name>jrserver</servlet-name>          <url-pattern>/jrserver/*</url-pattern>     </servlet-mapping>     <servlet-mapping>         <servlet-name>sendfile</servlet-name>         <url-pattern>/sendfile/*</url-pattern>     </servlet-mapping>     <servlet-mapping>         <servlet-name>dhtml</servlet-name>          <url-pattern>/dhtml/*</url-pattern>     </servlet-mapping>     <servlet-mapping>         <servlet-name>help</servlet-name>         <url-pattern>/help/*</url-pattern>      </servlet-mapping> </web-app> ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Integrating by Building a Logi JReport Server EAR

The self-contained Logi JReport Server can be deployed as a single EAR file.

For example, you can create a Logi JReport Server EAR file named Logi JReport.ear and the structure of the Logi JReport Server EAR is as follows:

**Logi JReport.ear**

META-INF/application.xml

Logi JReport-lib/ -**-** This folder contains all resources in the Logi JReport Server library.

Logi JReport.war

META-INF/MANIFEST.MF

WEB-INF/web.xml

admin/

jinfonet/

dhtmljsp/

Following the Java EE standard, you should configure the META-INF/application.xml file before deploying the EAR:

|  |
| --- |
| ``` <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE application PUBLIC "-//Sun Microsystems, Inc.//DTD J2EE Application 1.3//EN"  "http://java.sun.com/dtd/application_1_3.dtd"> <application>     <display-name>Self-contained Logi JReport Server</display-name>     <module id="Logi JReportWebModule">         <web>             <web-uri>Logi JReport.war</web-uri>             <context-root>Logi JReport</context-root>         </web>     </module> </application> ``` |

The contents in the web.xml of the Logi JReport Server EAR are the same as those in [web.xml of the Logi JReport Server WAR](#web).

Since the Logi JReport Server library is included in Logi JReport-lib of the EAR layer, you must specify Class-Path in the META-INF/MANIFEST.MF file. The contents below should be included in the MANIFEST.MF file:

`Class-Path: Logi JReport-lib/jrenv.jar Logi JReport-lib/JRESServlets.jar Logi JReport-lib/JREngine.jar ...`

Class-Path is a list of all packages in the Logi JReport Server library. Each package name should start with the prefix Logi JReport-lib/, and you should use a blank space to separate package names.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Integrating by Building a User WAR and Embedding a Self-Contained Logi JReport Server

You can embed a self-contained Logi JReport Server into your WAR.

For example, you can create a WAR named MyApp.war, and then embed a self-contained Logi JReport Server inside it. The structure of your WAR may be as follows:

**MyApp.war**

WEB-INF/

web.xml

lib/ -- This folder contains all resources in the Logi JReport Server library and your other jar files.

classes/ -- This folder contains your servlet classes.

../../asset/images/

jsp/

If you put the Logi JReport WAR related JSPs to a sub folder, for example Logi JReport, and this time the structure of your WAR may be as follows:

**MyApp.war**

WEB-INF/

web.xml

lib/ -- This folder contains all resources in the Logi JReport Server library and your other jar files.

classes/ -- This folder contains your servlet classes.

../../asset/images/

**Logi JReport/**

**admin/**

**dhtmljsp/**

**jinfonet/**

**...**

To run Logi JReport reports, you must add the following into WEB-INF/web.xml:

* Add the following entry:

  `<context-param>  
   <param-name>autoDetectServletPath</param-name>  
   <param-value>false</param-value>  
   </context-param>`
* Add listener as follows:

  `<listener>  
   <listener-class>jet.server.servlets.JRServerContextListener</listener-class>  
   </listener>`

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Integrating by Building a User EAR and Embedding a Self-Contained Logi JReport Server

You can embed a self-contained Logi JReport Server into your EAR in order to use Logi JReport Server from EJB.

For example, you can create an EAR named MyApp.ear and then embed a self-contained Logi JReport Server inside it. In the EAR, there is an EJB module used for initializing Logi JReport Server. The structure of your EAR may be as follows:

**MyEAR.ear**

META-INF/application.xml

Logi JReport-lib/ -- This folder contains all resources in the Logi JReport Server library

MyEjb.jar

META-INF/

MANIFEST.MF

ejb-jar.xml

com/

Following the Java EE standard, you should configure the META-INF/application.xml file before deploying your EAR:

|  |
| --- |
| ``` <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE application PUBLIC "-//Sun Microsystems, Inc.//DTD J2EE Application 1.3//EN"  "http://java.sun.com/dtd/application_1_3.dtd"> <application>     <display-name>EJB with Embedded Logi JReport Server</display-name>     <module id="MyEJBModule">         <ejb>MyEjb.jar</ejb>     </module> </application> ``` |

Since the Logi JReport Server library is included in the Logi JReport-lib folder of the EAR layer, you must specify Class-Path in the META-INF/MANIFEST.MF file. The contents below should be included in the MANIFEST.MF file:

`Class-Path: Logi JReport-lib/jrenv.jar Logi JReport-lib/JRESServlets.jar Logi JReport-lib/JREngine.jar ...`

Class-Path is a list of all packages in the Logi JReport Server library. Each package name should start with the prefix Logi JReport-lib/, and you should use a blank space to separate package names.

If you do not want to set the reporthome for the embedded self-contained Logi JReport Server, but instead want to use Logi JReport's default settings, there is no requirement for configuring the ejb-jar.xml. However, if you want to control the reporthome of the Logi JReport Server, or specify a JNDI data source for Logi JReport Server to use, you should first configure the ejb-jar.xml file using the `<env-entry></env-entry>` tags. For example:

|  |
| --- |
| ``` <?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE ejb-jar PUBLIC "-//Sun Microsystems, Inc.//DTD Enterprise JavaBeans 2.0//EN"  "http://java.sun.com/dtd/ejb-jar_2_0.dtd"> <ejb-jar id="ejb-jar_ID">     <display-name>MyEJB</display-name>     <enterprise-beans>         <session id="Logi JReportEJB">             <ejb-name>JRptServer</ejb-name>             <home>demo.JRptServerHome</home>             <remote>demo.JRptServer</remote>             <ejb-class>demo.JRptServerBean</ejb-class>             <session-type>Stateless</session-type>             <!-- Specify Logi JReport reporthome directly                 <env-entry>                 <env-entry-name>Logi JReport.rpthome</env-entry-name>                 <env-entry-value>/home/Logi JReport</env-entry-value>                 <env-entry-type>java.lang.String</env-entry-type>                 </env-entry>             -->             <!-- Logi JReport callback my CustomizedServerEnv -->             <env-entry>                 <env-entry-name>Logi JReport.servenv</env-entry-name>                 <env-entry-value>demo.Logi JReportServerEnv</env-entry-value>                 <env-entry-type>java.lang.String</env-entry-type>             </env-entry>             <transaction-type>Bean</transaction-type>         </session>     </enterprise-beans> </ejb-jar> ``` |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009673221-Specifying-Reporthome-for-Logi-JReport-Server-Guide-v15-Server-in-a-Java-EE-Environment)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009673041-Deploying-Logi-JReport-Server-Guide-v15-Server-to-a-Java-Application-Server)
