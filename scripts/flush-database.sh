#!/bin/bash

echo "Flushing database..." 
python manage.py flush --skip-checks --no-input
echo "Flush complete"
