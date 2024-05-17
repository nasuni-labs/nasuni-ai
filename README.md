# About

This repository contains a collection of scripts, tools, and documentation for integrating your Nasuni Storage with AI tools available in the market. These scripts, tools and documentation are references for how Nasuni customers can architect their environment to integrate with these third-party tools

# Support Statement

*   This package stack has only been validated with the component versions documented in the README file.
    
*   Nasuni Support is limited to Nasuni APIs and Protocols (SMB, NFS, SNMP, GFA Telemetry, Nasuni Access Anywhere Monitoring API). Nasuni API and Protocol bugs should be reported to Nasuni Customer Support.
    
*   GitHub project bugs, questions, and feature requests should be submitted as “Issues” in GitHub under its repositories.

# Microsoft Co-Pilot Studio

In the copilot/ directory of this repository you will find documentation and assistance scripts for integrating with Microsoft Copilot Studio to create your own copilots using data that resides in your Nasuni Storage. 

## Python Scripts

Co-pilot studio has a file size limit of 3MB for files that can be leveraged. Some larger PDF or HTML files with images can exeed that size limit. In the copilot/Scripts/ directory you will find example python scripts which can be used to extract just the test of pdf and html files to use with your custom Co-pilots. 

Each script contains a NASUNI_DIR and OUTPUT_DIR which you will want to update to specify your Source NASUNI_DIR, and the export location for our text/json files as the OUTPUT_DIR. 

# Microsoft Azure AI Pipelines

In the azureaipipelinnes/ directory of this repository you will find documentation and example scripts for more advanced integrations where your Nasuni Data is part of an AI Pipeline to feed data into Azure services like Azure AI and/or Azure AI Search. This will allow you to build your own custom pipelines to feed your AI workflow with AI tools beyond just Microsoft Co-pilot. 