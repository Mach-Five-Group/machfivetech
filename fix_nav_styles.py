#!/usr/bin/env python3
import os
import re

# List of files to check and update
files_to_update = [
    "services/culture/index.html",
    "services/delight/index.html", 
    "services/future-proof/index.html",
    "services/minds/index.html",
    "knowledge-base/index.html",
    "knowledge-base/scaling-microservices-at-mach-speed.html",
    "careers/index.html"
]

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update main-nav padding
        content = re.sub(r'\.main-nav\s*\{\s*background:\s*white;\s*padding:\s*20px\s*0;', 
                        '.main-nav {\n            background: white;\n            padding: 5px 0;', content)
        
        # Update nav-container grid-template-columns
        content = re.sub(r'grid-template-columns:\s*280px\s*auto\s*1fr;',
                        'grid-template-columns: 1fr auto 1fr;', content)
        
        # Update justify-self for main-nav .nav-logo
        content = re.sub(r'(\.main-nav\s+\.nav-logo\s*\{[^}]*?)justify-self:\s*start;',
                        r'\1justify-self: center;', content, flags=re.DOTALL)
        
        # Update nav-menu justify-self
        content = re.sub(r'(\.nav-menu\s*\{[^}]*?)justify-self:\s*center;',
                        r'\1justify-self: end;', content, flags=re.DOTALL)
        
        # Replace old nav-logo text styles with image styles
        old_nav_logo_pattern = r'\.nav-logo\s*\{[^}]*font-size:[^}]+\}[\s\n]*\.nav-logo\s+span\s*\{[^}]+\}'
        new_nav_logo_styles = '''        .nav-logo {
            display: inline-flex;
            align-items: center;
            text-decoration: none;
        }

        .nav-logo img {
            transition: opacity 0.2s ease;
        }

        .nav-logo:hover img {
            opacity: 0.8;
        }'''
        
        content = re.sub(old_nav_logo_pattern, new_nav_logo_styles, content, flags=re.DOTALL)
        
        # Add laptop viewport adjustment if not present
        laptop_media_query_pattern = r'(@media\s*\(min-width:\s*1024px\)\s*and\s*\(max-width:\s*1600px\)\s*\{[^}]*\.footer-bottom\s*\{[^}]+\}\s*)'
        if re.search(laptop_media_query_pattern, content, re.DOTALL) and 'Adjust top-bar-right position for laptop viewports' not in content:
            content = re.sub(laptop_media_query_pattern + r'(\s*\})',
                           r'\1\n            /* Adjust top-bar-right position for laptop viewports */\n            .top-bar-right {\n                margin-right: 150px;\n            }\2',
                           content, flags=re.DOTALL)
        
        # Only write if changes were made
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {filepath}")
        else:
            print(f"No changes needed: {filepath}")
            
    except Exception as e:
        print(f"Error updating {filepath}: {e}")

# Update all files
for file in files_to_update:
    if os.path.exists(file):
        update_file(file)
    else:
        print(f"File not found: {file}")

print("\nAll files processed!")