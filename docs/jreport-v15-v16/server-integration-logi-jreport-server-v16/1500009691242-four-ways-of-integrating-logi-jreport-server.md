---
title: "Four Ways of Integrating Logi JReport Server"
id: 1500009691242
section: "Server Integration Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691242-Four-Ways-of-Integrating-Logi-JReport-Server
updated_at: 2021-11-03T06:56:58Z
---

# Four Ways of Integrating Logi JReport Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717521-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717341-Deploying-Logi-Report-Server-to-a-Java-Application-Server)

# Four Ways of Integrating Logi JReport Server

To integrate Logi JReport Server with your application server, you can either create a Logi JReport Server WAR/EAR, or create your WAR/EAR and embed a self-contained Logi JReport Server inside it. For how to create a Logi JReport Server WAR/EAR, see [Building a WAR/EAR file to Include a Self-contained Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009717561-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

Below is a list of the sections covered in this topic:

* [Integrating by Building a Logi JReport Server WAR](#Way1)
* [Integrating by Building a Logi JReport Server EAR](#Way2)
* [Integrating by Building a User WAR and Embedding a Self-contained Logi JReport Server](#Way3)
* [Integrating by Building a User EAR and Embedding a Self-contained Logi JReport Server](#Way4)

## Integrating by Building a Logi JReport Server WAR

The self-contained Logi JReport Server can be deployed as a single WAR file.

For example, you can create a Logi JReport Server WAR file named jreport.war and the structure of the Logi JReport Server WAR is as follows:

**jreport.war**

WEB-INF/

web.xml

lib/ -- This folder contains all resources in the Logi JReport Server library.

admin/ -- This folder contains JSP files for administration tasks on the Logi JReport Server console.

jinfonet/ -- This folder contains JSP files for the Logi JReport Server console.

dhtmljsp/ --This folder contains JSP files for viewing page reports.

The following is a sample of the content in the web.xml file of the Logi JReport Server WAR:

```
<?xml version="1.0" encoding="ISO-8859-1"?>   
<!DOCTYPE web-app PUBLIC "-//Sun Microsystems,   
Inc.//DTD Web Application 2.3//EN"   
"http://java.sun.com/dtd/web-app_2_3.dtd">   
<web-app>  
    <listener>   
        <listener-class>jet.server.servlets.JRServerContextListener</listener-class>  
    </listener>  
    <servlet>  
        <servlet-name>jrserver</servlet-name>  
        <servlet-class>jet.server.servlets.JRServlet</servlet-class>  
    </servlet>  
    <servlet>  
        <servlet-name>sendfile</servlet-name>  
        <servlet-class>jet.server.servlets.SendFileServlet</servlet-class>  
    </servlet>  
    <servlet>  
        <servlet-name>dhtml</servlet-name>  
        <servlet-class>jet.web.dhtml.DHTMLlet</servlet-class>  
    </servlet>  
    <servlet>  
        <servlet-name>help</servlet-name>  
        <servlet-class>jet.web.dhtml.JHelplet</servlet-class>   
    </servlet>  
    <servlet-mapping>  
        <servlet-name>jrserver</servlet-name>   
        <url-pattern>/jrserver/*</url-pattern>  
    </servlet-mapping>  
    <servlet-mapping>  
        <servlet-name>sendfile</servlet-name>  
        <url-pattern>/sendfile/*</url-pattern>  
    </servlet-mapping>  
    <servlet-mapping>  
        <servlet-name>dhtml</servlet-name>   
        <url-pattern>/dhtml/*</url-pattern>  
    </servlet-mapping>  
    <servlet-mapping>  
        <servlet-name>help</servlet-name>  
        <url-pattern>/help/*</url-pattern>   
    </servlet-mapping>  
</web-app>
```

## Integrating by Building a Logi JReport Server EAR

The self-contained Logi JReport Server can be deployed as a single EAR file.

For example, you can create a Logi JReport Server EAR file named jreport.ear and the structure of the Logi JReport Server EAR is as follows:

**jreport.ear**

META-INF/application.xml

jreport-lib/ -**-** This folder contains all resources in the Logi JReport Server library.

jreport.war

META-INF/MANIFEST.MF

WEB-INF/web.xml

admin/

jinfonet/

dhtmljsp/

Following the Java EE standard, you should configure the META-INF/application.xml file before deploying the EAR:

```
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE application PUBLIC "-//Sun Microsystems, Inc.//DTD J2EE Application 1.3//EN"   
"http://java.sun.com/dtd/application_1_3.dtd">  
<application>  
    <display-name>Self-contained JReport Server</display-name>  
    <module id="JReportWebModule">  
        <web>  
            <web-uri>jreport.war</web-uri>  
            <context-root>jreport</context-root>  
        </web>  
    </module>  
</application>
```

The contents in the web.xml of the Logi JReport Server EAR are the same as those in [web.xml of the Logi JReport Server WAR](#web).

Since the Logi JReport Server library is included in jreport-lib of the EAR layer, you must specify Class-Path in the META-INF/MANIFEST.MF file. The contents below should be included in the MANIFEST.MF file:

`Class-Path: jreport-lib/jrenv.jar jreport-lib/JRESServlets.jar jreport-lib/JREngine.jar ...`

Class-Path is a list of all packages in the Logi JReport Server library. Each package name should start with the prefix jreport-lib/, and you should use a blank space to separate package names.

## Integrating by Building a User WAR and Embedding a Self-contained Logi JReport Server

You can embed a self-contained Logi JReport Server into your WAR.

For example, you can create a WAR named MyApp.war, and then embed a self-contained Logi JReport Server inside it. The structure of your WAR may be as follows:

**MyApp.war**

WEB-INF/

web.xml

lib/ -- This folder contains all resources in the Logi JReport Server library and your other jar files.

classes/ -- This folder contains your servlet classes.

../../asset/images/

jsp/

If you put the Logi JReport WAR related JSPs to a sub folder, for example jreport, and this time the structure of your WAR may be as follows:

**MyApp.war**

WEB-INF/

web.xml

lib/ -- This folder contains all resources in the Logi JReport Server library and your other jar files.

classes/ -- This folder contains your servlet classes.

../../asset/images/

**jreport/**

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

## Integrating by Building a User EAR and Embedding a Self-contained Logi JReport Server

You can embed a self-contained Logi JReport Server into your EAR in order to use Logi JReport Server from EJB.

For example, you can create an EAR named MyApp.ear and then embed a self-contained Logi JReport Server inside it. In the EAR, there is an EJB module used for initializing Logi JReport Server. The structure of your EAR may be as follows:

**MyEAR.ear**

META-INF/application.xml

jreport-lib/ -- This folder contains all resources in the Logi JReport Server library

MyEjb.jar

META-INF/

MANIFEST.MF

ejb-jar.xml

com/

Following the Java EE standard, you should configure the META-INF/application.xml file before deploying your EAR:

```
<?xml version="1.0" encoding="UTF-8"?>  

<!DOCTYPE application PUBLIC "-//Sun Microsystems, Inc.//DTD J2EE Application 1.3//EN"   

"http://java.sun.com/dtd/application_1_3.dtd">  

<application>  

    <display-name>EJB with Embedded JReport Server</display-name>  

    <module id="MyEJBModule">  

        <ejb>MyEjb.jar</ejb>  

    </module>  

</application>
```

Since the Logi JReport Server library is included in the jreport-lib folder of the EAR layer, you must specify Class-Path in the META-INF/MANIFEST.MF file. The contents below should be included in the MANIFEST.MF file:

`Class-Path: jreport-lib/jrenv.jar jreport-lib/JRESServlets.jar jreport-lib/JREngine.jar ...`

Class-Path is a list of all packages in the Logi JReport Server library. Each package name should start with the prefix Logi JReport-lib/, and you should use a blank space to separate package names.

If you do not want to set the reporthome for the embedded self-contained Logi JReport Server, but instead want to use Logi JReport's default settings, there is no requirement for configuring the ejb-jar.xml. However, if you want to control the reporthome of Logi JReport Server, or specify a JNDI data source for Logi JReport Server to use, you should first configure the ejb-jar.xml file using the <env-entry></env-entry> tags. For example:

```
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE ejb-jar PUBLIC "-//Sun Microsystems, Inc.//DTD Enterprise JavaBeans 2.0//EN"   
"http://java.sun.com/dtd/ejb-jar_2_0.dtd">  
<ejb-jar id="ejb-jar_ID">  
    <display-name>MyEJB</display-name>  
    <enterprise-beans>  
        <session id="JReportEJB">  
            <ejb-name>JRptServer</ejb-name>  
            <home>demo.JRptServerHome</home>  
            <remote>demo.JRptServer</remote>  
            <ejb-class>demo.JRptServerBean</ejb-class>  
            <session-type>Stateless</session-type>  
            <!-- Specify Logi JReport reporthome directly  
                <env-entry>  
                <env-entry-name>jreport.rpthome</env-entry-name>  
                <env-entry-value>/home/jreport</env-entry-value>  
                <env-entry-type>java.lang.String</env-entry-type>  
                </env-entry>  
            -->  
            <!-- Logi JReport callback my CustomizedServerEnv -->  
            <env-entry>  
                <env-entry-name>jreport.servenv</env-entry-name>  
                <env-entry-value>demo.JReportServerEnv</env-entry-value>  
                <env-entry-type>java.lang.String</env-entry-type>  
            </env-entry>  
            <transaction-type>Bean</transaction-type>  
        </session>  
    </enterprise-beans>  
</ejb-jar>
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009717521-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009717341-Deploying-Logi-Report-Server-to-a-Java-Application-Server)
