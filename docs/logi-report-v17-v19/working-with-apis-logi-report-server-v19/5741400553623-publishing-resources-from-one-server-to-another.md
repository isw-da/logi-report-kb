---
title: "Publishing Resources from One Server to Another"
id: 5741400553623
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741400553623-Publishing-Resources-from-One-Server-to-Another
updated_at: 2022-10-31T17:15:51Z
---

# Publishing Resources from One Server to Another

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741415368343-Using-RMI-in-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741386771735-Working-with-Resource-Versions)

# Publishing Resources from One Server to Another

You can [publish resources](https://devnet.logianalytics.com/hc/en-us/articles/5741453495191-Publishing-Resources#ToServer) in the resource tree of a Logi Report Server (source server) to another Logi Report Server (target server), using the [TargetServerManager](#TargetServerManager) and [TargetServer](#TargetServer) objects in the jet.server.api package of the Server API. This topic describes the methods in TargetServerManager and TargetServer.

## TargetServerManager

The TargetServerManager object manages the TargetServer objects. You can get it using the method *RptServer.getTargetServerManager()*.

See the methods in TargetServerManager:

* String createTargetServer(user, connectionProp)  
  Creates the TargetServer object for the specified user using the designated connection properties. Returns the ID for the newly created TargetServer
  object; or throws exception when
  connectionProp is invalid.
  + user - The username used to sign in to the target server.
  + connectionProp - A property that contains the connection information.
* TargetServer getTargetServer(ID)  
  Gets the TargetServer object of the specified ID.
  Returns null if there is not the
  TargetServer object for the current user; or throws exception when the
  TargetServer object is invalid.
  + ID - The ID of the TargetServer object.
* void deleteTargetServer(ID)  
  Deletes the TargetServer object of the specified ID.
  + ID - The ID of the TargetServer object.
* Properties getConnectionProp(ID)  
  Gets the connection properties stored in the specified TargetServer object.
  + ID - The ID of the TargetServer object.

## TargetServer

The TargetServer object indicates the target server. It contains username and connection properties. Each username corresponds to one TargetServer object.

See the methods in TargetServer:

* void connect()  
  Signs in to the target server where to publish resources and creates a new session.
* void disconnect()  
  Signs out of the target server and removes the session.
* String getFolderTree(permissions)  
  Gets the JSON string of the target server resource folder tree according to the specified permissions.
  + permission - The permissions the signed-in user has on the target server folders.
* boolean resourceExists(path)  
  Returns
  whether the specified path node exists on the target server resource tree.
  + path - The path on the target server resource tree.
* String getPermission(path)  
  Gets the binary string of the permissions the signed-in user has on the specified path.
  + path - The path on the target server resource tree.
* void setPermission(path, permissions)  
  Sets permissions for the signed-in user on the specified target server path.
  + path - The path on the target server resource tree.
  + permissions - The permissions the signed-in user has on the specified path.
* void addResourceFile(path, resourceName, fromFile, properties, permissions)  
  Publishes the specified resource file to the designated path on the target server.
  + path - The path on the target server resource tree where to publish resources.
  + resourceName - The node name for the to-be-published resources on the target server.
  + fromFile - The compressed file that contains the resources you want to publish.
  + properties - The properties of the to-be-published resources.
  + permissions - The user permissions for the to-be-published resources.
* void createFolder(path, resourceName, properties, permissions)  
  Creates folder on the target server.
  + path - The path on the target server resource tree where to create the folder.
  + resourceName - The name of the new folder.
  + properties - The properties of the new folder.
  + permissions - The user permissions for the new folder.
* Properties getResourceProperties(path)  
  Gets the properties of the specified path on the target server.
  + path - The path on the target server resource tree.
* void setResourceProperties(path, properties)  
  Sets properties for the specified path on the target server.
  + path - The path on the target server resource tree.
  + properties - The properties of the resource path.
* void deleteResource(path)  
  Deletes the specified path from the target server.
  + path - The path on the target server resource tree.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741415368343-Using-RMI-in-Logi-Report-Server)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741386771735-Working-with-Resource-Versions)
