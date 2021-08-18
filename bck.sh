#!/bin/bash
DATE=$(date +%Y-%m-%d-%H%M%S)
BACKUP_DIR="$HOME/backup"
SOURCE="$1"
tar -cvzpf $BACKUP_DIR/backup-$DATE.tar.gz $SOURCE
