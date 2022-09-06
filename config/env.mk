# This environment file is sourced from the Makefiles in this project
# it is in Makefile format (not shell)

# bucket name and prefix path used to store templates, data, scripts and
# build artifacts
# NOTE: S3 path should match the BootstrapBucket and BootstrapPrefix parameters
# in master.yaml template
export BOOTSTRAP_BUCKET_PATH ?= aws-bigdata-blog/artifacts/aws-lex-web-ui/artifacts

# S3 bucket hosting the web application
# The Makefile in the root dir can sync the local files to it
export WEBAPP_BUCKET ?= $()

# AWS cli env variables used when running/building
# Override by setting it in the environment before running make
export AWS_DEFAULT_PROFILE ?= default
export AWS_DEFAULT_REGION ?= us-east-1

# lex-web-ui config variables
export BOT_NAME ?= OrderFlowers
# set to empty if not present in environment
export POOL_ID ?= $()

# amazon-connect config variables
export CONNECT_CONTACT_FLOW_ID ?= $()
export CONNECT_INSTANCE_ID ?= $()
export CONNECT_API_GATEWAY_ENDPOINT ?= $()
export CONNECT_WAIT_FOR_AGENT_MESSAGE ?= $()
export CONNECT_PROMPT_FOR_NAME_MESSAGE ?= $()
export CONNECT_WAIT_FOR_AGENT_MESSAGE_INTERVAL_IN_SECONDS ?= $()
export CONNECT_AGENT_JOINED_MESSAGE ?= $()
export CONNECT_AGENT_LEFT_MESSAGE ?= $()
export CONNECT_CHAT_ENDED_MESSAGE ?= $()
export CONNECT_ATTACH_CHAT_TRANSCRIPT ?= $()

export BOT_INITIAL_TEXT ?= $()
export BOT_INITIAL_SPEECH ?= $()
export BOT_INITIAL_UTTERANCE ?= $()
export UI_TOOLBAR_TITLE ?= $()
export UI_TOOLBAR_LOGO ?= $()

export IFRAME_ORIGIN ?= $()
export PARENT_ORIGIN ?= $()

export VERSION := v$(shell node -p "const fs=require('fs');const path='./package.json';fs.existsSync(path)?require('./package.json').version : require('../package.json').version")
