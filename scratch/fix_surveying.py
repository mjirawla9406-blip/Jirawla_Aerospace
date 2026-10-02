import sys

with open('surveying-mapping.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace colors in the remaining sections

# Section 4: Video
content = content.replace('<section class="w-full bg-charcoal text-off-white py-24 relative overflow-hidden">', '<section class="w-full bg-inverse-surface text-inverse-on-surface py-24 relative overflow-hidden">')
content = content.replace('text-alert-red mb-4 block', 'text-tertiary mb-4 block')
content = content.replace('bg-charcoal border-charcoal/20', 'bg-inverse-surface border-inverse-surface')
content = content.replace('bg-alert-red text-charcoal', 'bg-tertiary text-on-tertiary')
content = content.replace('bg-alert-red', 'bg-tertiary')
content = content.replace('text-alert-red', 'text-tertiary')
content = content.replace('text-charcoal', 'text-on-surface')

# Section 5: Why Jirawla
content = content.replace('<section class="bg-off-white py-24 border-b border-light-grey">', '<section class="bg-surface-container-lowest py-24 border-b border-outline-variant/20">')
content = content.replace('bg-soft-rose', 'bg-tertiary/10')
content = content.replace('text-alert-red', 'text-tertiary')
content = content.replace('text-secondary', 'text-on-surface-variant')
content = content.replace('border-light-grey', 'border-outline-variant/30')
content = content.replace('hover:border-charcoal/30', 'hover:border-outline-variant')
content = content.replace('bg-off-white', 'bg-surface-container-lowest')
content = content.replace('bg-light-grey/40', 'bg-surface-container-low')
content = content.replace('border-alert-red/20', 'border-tertiary/20')

# Section 7: Final CTA
content = content.replace('<section class="bg-charcoal text-off-white py-24 text-center">', '<section class="bg-surface-container py-24 text-center">')
content = content.replace('<h2 class="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-off-white mb-6 tracking-tight">Ready to map your site?</h2>', '<h2 class="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface mb-6 tracking-tight">Ready to map your site?</h2>')
content = content.replace('<button class="bg-alert-red text-on-alert-red', '<button class="bg-primary text-on-primary')
content = content.replace('hover:bg-alert-red/90', 'hover:bg-surface-tint')

# Specific footer fix (from index.html)
footer_html = """<!-- Footer -->
<footer class="bg-surface-container-lowest border-t border-outline-variant/20 py-16">
<div class="max-w-container-max mx-auto px-margin-mobile md:px-margin-desktop grid grid-cols-1 md:grid-cols-4 gap-12">
    <!-- Brand Col -->
    <div class="col-span-1 md:col-span-1">
        <img src="Logo_Horizontal_Perfect.png" alt="Jirawla Aerospace" class="h-8 w-auto mb-6 grayscale opacity-80" />
        <p class="font-body-md text-body-md text-on-surface-variant max-w-xs">
            Industrial drone automation for security, surveillance, and heavy industry.
        </p>
    </div>
    <!-- Links Col 1 -->
    <div>
        <h4 class="font-label-caps text-label-caps text-on-surface font-semibold uppercase tracking-widest mb-4 block">Solutions</h4>
        <ul class="flex flex-col gap-3 font-body-md text-body-md text-on-surface-variant">
            <li><a href="surveillance-security.html" class="hover:text-primary transition-colors">Surveillance &amp; Security</a></li>
            <li><a href="surveying-mapping.html" class="hover:text-primary transition-colors">Surveying &amp; Mapping</a></li>
        </ul>
    </div>
    <!-- Links Col 2 -->
    <div>
        <h4 class="font-label-caps text-label-caps text-on-surface font-semibold uppercase tracking-widest mb-4 block">Company</h4>
        <ul class="flex flex-col gap-3 font-body-md text-body-md text-on-surface-variant">
            <li><a href="index.html#about" class="hover:text-primary transition-colors">About Us</a></li>
            <li><a href="#" class="hover:text-primary transition-colors">Careers</a></li>
            <li><a href="#" class="hover:text-primary transition-colors">Contact</a></li>
        </ul>
    </div>
    <!-- Socials / Legal -->
    <div>
        <h4 class="font-label-caps text-label-caps text-on-surface font-semibold uppercase tracking-widest mb-4 block">Connect</h4>
        <div class="flex items-center gap-4 mb-8">
            <a href="#" class="text-on-surface-variant hover:text-primary transition-colors">
                <span class="material-symbols-outlined">share</span>
            </a>
            <a href="#" class="text-on-surface-variant hover:text-primary transition-colors">
                <span class="material-symbols-outlined">mail</span>
            </a>
        </div>
        <p class="font-body-md text-sm text-on-surface-variant opacity-60">
            &copy; 2024 Jirawla Aerospace.<br/>All rights reserved.
        </p>
    </div>
</div>
</footer>"""

start_footer = content.find('<footer')
end_footer = content.find('</footer>') + len('</footer>')

content = content[:start_footer] + footer_html + content[end_footer:]

with open('surveying-mapping.html', 'w', encoding='utf-8') as f:
    f.write(content)
