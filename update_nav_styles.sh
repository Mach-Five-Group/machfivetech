#!/bin/bash

# List of files to update
files=(
    "services/code/index.html"
    "services/culture/index.html"
    "services/delight/index.html"
    "services/future-proof/index.html"
    "services/minds/index.html"
    "services/plan/index.html"
    "knowledge-base/index.html"
    "knowledge-base/scaling-microservices-at-mach-speed.html"
    "careers/index.html"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "Updating $file..."
        
        # Update main-nav padding
        sed -i '' 's/padding: 20px 0;/padding: 5px 0;/g' "$file"
        
        # Update nav-container to use grid layout
        sed -i '' 's/display: flex;$/display: grid;/g' "$file"
        sed -i '' 's/justify-content: center;$/grid-template-columns: 1fr auto 1fr;/g' "$file"
        
        # Update nav-logo CSS to use image instead of text
        sed -i '' '/.nav-logo {/,/^        }/c\
        .nav-logo {\
            display: inline-flex;\
            align-items: center;\
            text-decoration: none;\
        }\
\
        .nav-logo img {\
            transition: opacity 0.2s ease;\
        }\
\
        .nav-logo:hover img {\
            opacity: 0.8;\
        }' "$file"
        
        # Remove the nav-logo span styles
        sed -i '' '/.nav-logo span {/,/^        }/d' "$file"
        
        # Update nav-menu to justify-self: end
        sed -i '' 's/justify-self: center;/justify-self: end;/g' "$file"
        
        # Add margin-right to top-bar-right
        sed -i '' '/\.top-bar-right {/,/}/ s/align-items: center;/align-items: center;\
            margin-right: 200px;/g' "$file"
        
        echo "Updated $file"
    fi
done

echo "All files updated!"