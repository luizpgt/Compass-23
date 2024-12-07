#!/bin/bash

ENV_FILE="./../visao-computacional/.env"
if test -f "$ENV_FILE"; then
  source $ENV_FILE
  if [[ -z "$BUCKET_NAME" ]]; then
    echo "BUCKET_NAME not found on $ENV_FILE"
  else
    if ! command -v aws &> /dev/null
    then
      echo "Make sure to have AWS installed and properly configurated"
      exit 1
    else
      aws s3 sync ./images/ s3://${BUCKET_NAME}
      echo "File sync completed!"
    fi
  fi
else 
  echo "Unable to locate '$ENV_FILE'"
fi

# usage: sync files from ./images/ to s3 =|= upload missing files to s3 
# non-default tip: usage of --delete flag on 'aws' cli deletes images on s3 and not in ./images/