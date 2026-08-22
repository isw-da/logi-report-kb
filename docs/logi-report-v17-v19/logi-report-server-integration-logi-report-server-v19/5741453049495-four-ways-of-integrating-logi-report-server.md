---
title: "Four Ways of Integrating Logi Report Server"
id: 5741453049495
section: "Logi Report Server Integration Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741453049495-Four-Ways-of-Integrating-Logi-Report-Server
updated_at: 2022-10-31T17:17:59Z
---

# Four Ways of Integrating Logi Report Server

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741467928983-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741431629463-Deploying-Logi-Report-Server-to-a-Java-Application-Server)

# Four Ways of Integrating Logi Report Server

To integrate Logi Report Server with your application server, you can either create a Logi Report Server WAR/EAR, or create your WAR/EAR and embed a self-contained Logi Report Server inside it. This topic describes how you can integrate Logi Report Server with your application server using four ways.

For how to create a Logi Report Server WAR/EAR, see [Building a WAR/EAR file to Include a Self-contained Logi Report Server](https://devnet.logianalytics.com/hc/en-us/articles/5741473837719-Building-a-WAR-EAR-File-to-Include-a-Self-contained-Logi-Report-Server).

This topic contains the following sections:

* [Integrating by Building a Logi Report Server WAR](#Way1)
* [Integrating by Building a Logi Report Server EAR](#Way2)
* [Integrating by Building a User WAR and Embedding a Self-contained Logi Report Server](#Way3)
* [Integrating by Building a User EAR and Embedding a Self-contained Logi Report Server](#Way4)

## Integrating by Building a Logi Report Server WAR

You can deploy the self-contained Logi Report Server as a single WAR file.

For example, you can create a Logi Report Server WAR file named **jreport.war** and the structure of the Logi Report Server WAR is:

**jreport.war**

WEB-INF/

web.xml

lib/ -- This folder contains the resources in the Logi Report Server library.

admin/ -- This folder contains JSP files for administration tasks on the Logi Report Server Console.

jinfonet/ -- This folder contains JSP files for the Logi Report Server Console.

dhtmljsp/ --This folder contains JSP files for viewing page reports.

See the following sample of the contents in the **web.xml** file of the Logi Report Server WAR:

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

## Integrating by Building a Logi Report Server EAR

You can deploy the self-contained Logi Report Server as a single EAR file.

For example, you can create a Logi Report Server EAR file named **jreport.ear** and the structure of the Logi Report Server EAR is:

**jreport.ear**

META-INF/application.xml

jreport-lib/ -- This folder contains the resources in the Logi Report Server library.

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

The contents in the web.xml of the Logi Report Server EAR are the same as those in [web.xml of the Logi Report Server WAR](#web).

Since the Logi Report Server library is included in jreport-lib of the EAR layer, you must specify Class-Path in the META-INF/MANIFEST.MF file. Add the following contents in the MANIFEST.MF file:

`Class-Path: jreport-lib/jrenv.jar jreport-lib/JRESServlets.jar jreport-lib/JREngine.jar ...`

Class-Path is a list of the packages in the Logi Report Server library. Each package name should start with the prefix **jreport-lib/**, and you should use a blank space to separate the package names.

## Integrating by Building a User WAR and Embedding a Self-contained Logi Report Server

You can embed a self-contained Logi Report Server into your WAR.

For example, you can create a WAR named **MyApp.war**, and then embed a self-contained Logi Report Server inside it. The structure of your WAR may be:

**MyApp.war**

WEB-INF/

web.xml

lib/ -- This folder contains the resources in the Logi Report Server library and your other jar files.

classes/ -- This folder contains your servlet classes.

../../asset/images/

jsp/

If you put the Logi Report WAR related JSPs to a subfolder, for example **jreport**, the structure of your WAR may be:

**MyApp.war**

WEB-INF/

web.xml

lib/ -- This folder contains the resources in the Logi Report Server library and your other jar files.

classes/ -- This folder contains your servlet classes.

../../asset/images/

**jreport/**

**admin/**

**dhtmljsp/**

**jinfonet/**

**...**

To run Logi Report reports, you need to add the following into WEB-INF/web.xml:

* Add the following entry:

  ```
  <context-param>  
      <param-name>autoDetectServletPath</param-name>  
      <param-value>false</param-value>  
  </context-param>
  ```
* Add listener:

  ```
  <listener>  
      <listener-class>jet.server.servlets.JRServerContextListener</listener-class>  
  </listener>
  ```
* Add filter and servlet:

  ```
  <filter>  
      <filter-name>Character Encoding</filter-name>  
      <filter-class>jet.server.servlets.CharacterEncodingFilter</filter-class>  
      <init-param>  
          <param-name>encoding</param-name>  
          <param-value>UTF-8</param-value>  
      </init-param>  
      <init-param>  
          <param-name>excludedFiles</param-name>  
          <param-value>.css,.js,.png,.svg,.pdf,.rtf,.xls,.xml,.xlsx,.gif,.ico,.rpt,.cls,.jpg,.jpeg,.zip,.jz</param-value>  
      </init-param>  
  </filter>  
    
  <filter>  
      <filter-name>JzFileFilter</filter-name>  
      <filter-class>com.jinfonet.web.client.RespHeaderFilter</filter-class>  
      <init-param>  
          <param-name>Content-Type</param-name>  
          <param-value>application/x-javascript</param-value>  
      </init-param>  
      <init-param>  
          <param-name>Content-Encoding</param-name>  
          <param-value>gzip</param-value>  
      </init-param>  
  </filter>  
    
  <filter-mapping>  
      <filter-name>JzFileFilter</filter-name>  
      <url-pattern>*.jz</url-pattern>  
  </filter-mapping>  
    
  <filter-mapping>  
      <filter-name>Character Encoding</filter-name>  
      <url-pattern>/*</url-pattern>  
  </filter-mapping>  
    
  <servlet>  
      <servlet-name>jrserver</servlet-name>  
      <servlet-class>jet.server.servlets.JRServlet</servlet-class>  
  <!--</servlet>  
    
  <servlet>  
      <servlet-name>JRWSServlet</servlet-name>  
      <display-name>Logi Report Webservice Servlet</display-name>  
      <servlet-class>  
          jet.server.ws.xfire.servlets.JRWebServiceServlet  
      </servlet-class>-->  
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
      <servlet-name>WebOSServlet</servlet-name>  
      <display-name>WebOSServlet</display-name>  
      <servlet-class>com.jinfonet.web.client.WebOSServlet</servlet-class>  
  </servlet>  
    
  <servlet-mapping>  
      <servlet-name>jrserver</servlet-name>  
      <url-pattern>/jrserver/*</url-pattern>  
  <!-- </servlet-mapping>  
    
  <servlet-mapping>  
      <servlet-name>JRWSServlet</servlet-name>  
      <url-pattern>/services/*</url-pattern>-->  
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
      <servlet-name>WebOSServlet</servlet-name>  
      <url-pattern>*.do</url-pattern>  
  </servlet-mapping>  
     
  <servlet-mapping>  
      <servlet-name>WebOSServlet</servlet-name>  
      <url-pattern>*.vt</url-pattern>  
  </servlet-mapping>  
    
  <servlet-mapping>  
      <servlet-name>WebOSServlet</servlet-name>  
      <url-pattern>/vt/*</url-pattern>  
  </servlet-mapping>
  ```

## Integrating by Building a User EAR and Embedding a Self-contained Logi Report Server

You can embed a self-contained Logi Report Server into your EAR in order to use Logi Report Server from EJB.

For example, you can create an EAR named **MyApp.ear** and then embed a self-contained Logi Report Server inside it. In the EAR, there is an EJB module used for initializing Logi Report Server. The structure of your EAR may be:

**MyEAR.ear**

META-INF/application.xml

jreport-lib/ -- This folder contains the resources in the Logi Report Server library.

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
    <display-name>EJB with Embedded Logi Report Server</display-name>  
    <module id="MyEJBModule">  
        <ejb>MyEjb.jar</ejb>  
    </module>  
</application>
```

Since the Logi Report Server library is included in the jreport-lib folder of the EAR layer, you must specify Class-Path in the META-INF/MANIFEST.MF file. Add the following contents in the MANIFEST.MF file:

`Class-Path: jreport-lib/jrenv.jar jreport-lib/JRESServlets.jar jreport-lib/JREngine.jar ...`

Class-Path is a list of the packages in the Logi Report Server library. Each package name should start with the prefix **jreport-lib/**, and you should use a blank space to separate the package names.

If you do not want to set the reporthome for the embedded self-contained Logi Report Server, but instead want to use Logi Report's default settings, there is no requirement for configuring the ejb-jar.xml. However, if you want to control the reporthome of Logi Report Server, or specify a JNDI data source for Logi Report Server to use, you should first configure the ejb-jar.xml file using the <env-entry></env-entry> tags. For example:

```
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE ejb-jar PUBLIC "-//Sun Microsystems, Inc.//DTD Enterprise JavaBeans 2.0//EN"   
"http://java.sun.com/dtd/ejb-jar_2_0.dtd">  
<ejb-jar id="ejb-jar_ID">  
    <display-name>MyEJB</display-name>  
    <enterprise-beans>  
        <session id="LogiReportEJB">  
            <ejb-name>JRptServer</ejb-name>  
            <home>demo.JRptServerHome</home>  
            <remote>demo.JRptServer</remote>  
            <ejb-class>demo.JRptServerBean</ejb-class>  
            <session-type>Stateless</session-type>  
            <!-- Specify Logi Report reporthome directly  
                <env-entry>  
                <env-entry-name>jreport.rpthome</env-entry-name>  
                <env-entry-value>/home/jreport</env-entry-value>  
                <env-entry-type>java.lang.String</env-entry-type>  
                </env-entry>  
            -->  
            <!-- Logi Report callback my CustomizedServerEnv -->  
            <env-entry>  
                <env-entry-name>jreport.servenv</env-entry-name>  
                <env-entry-value>demo.LogiReportServerEnv</env-entry-value>  
                <env-entry-type>java.lang.String</env-entry-type>  
            </env-entry>  
            <transaction-type>Bean</transaction-type>  
        </session>  
    </enterprise-beans>  
</ejb-jar>
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741467928983-Specifying-Reporthome-for-Logi-Report-Server-in-a-Java-EE-Environment)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741431629463-Deploying-Logi-Report-Server-to-a-Java-Application-Server)
