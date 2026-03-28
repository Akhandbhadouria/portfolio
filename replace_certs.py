import sys

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = "<!-- ========== CERTIFICATES — Horizontal Scroll ========== -->"
end_marker = "<!-- ========== EDUCATION SECTION ========== -->"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx == -1:
    print("Start marker not found")
    sys.exit(1)
if end_idx == -1:
    print("End marker not found")
    sys.exit(1)

replacement_string = """<!-- ========== CERTIFICATES — Stack & Info Area ========== -->
        <style>
            .new-certs-section {
                position: relative;
                padding: 120px 28px;
                background: var(--bg);
                display: flex;
                justify-content: center;
                border-top: 1px solid var(--border);
                font-family: 'DM Sans', sans-serif;
                overflow: hidden;
            }

            .new-certs-container {
                max-width: 1000px;
                width: 100%;
                display: grid;
                grid-template-columns: 1.1fr 0.9fr;
                gap: 80px;
                align-items: center;
                position: relative;
            }

            /* CROSSHAIR */
            .nc-crosshair {
                position: absolute;
                top: -40px;
                right: 38%;
                width: 20px;
                height: 20px;
                opacity: 0.3;
                pointer-events: none;
            }
            .nc-crosshair::before, .nc-crosshair::after {
                content: '';
                position: absolute;
                background: #fff;
            }
            .nc-crosshair::before {
                top: 50%; left: 0; right: 0; height: 1px; transform: translateY(-50%);
            }
            .nc-crosshair::after {
                left: 50%; top: 0; bottom: 0; width: 1px; transform: translateX(-50%);
            }
            .nc-crosshair-circle {
                position: absolute;
                top: 50%; left: 50%;
                width: 8px; height: 8px;
                border: 1px solid #fff;
                border-radius: 50%;
                transform: translate(-50%, -50%);
            }

            /* LEFT: VISUAL STACK */
            .nc-visuals {
                position: relative;
                width: 100%;
                height: 380px;
                display: flex;
                align-items: center;
                justify-content: center;
                perspective: 1000px;
            }

            .nc-card {
                position: absolute;
                width: 440px;
                height: 310px;
                border-radius: 12px;
                background: #111;
                overflow: hidden;
                transition: transform 0.6s cubic-bezier(0.2, 0.8, 0.2, 1), opacity 0.6s ease, z-index 0s;
                box-shadow: 0 10px 40px rgba(0,0,0,0.8);
                opacity: 0;
                pointer-events: none;
                border: 1px solid rgba(255,255,255,0.05);
            }

            .nc-card img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                object-position: center top;
            }

            .nc-card.bg-2 {
                transform: translate(-45px, 20px) rotate(-8deg) scale(0.85);
                z-index: 1;
                opacity: 0.4;
                filter: brightness(0.4);
            }

            .nc-card.bg-1 {
                transform: translate(60px, -15px) rotate(8deg) scale(0.9);
                z-index: 2;
                opacity: 0.7;
                filter: brightness(0.6);
            }

            .nc-card.active {
                transform: translate(0, 0) rotate(0deg) scale(1);
                z-index: 3;
                opacity: 1;
                pointer-events: auto;
                box-shadow: 0 0 50px rgba(0, 229, 181, 0.15), 0 0 0 2px rgba(0, 229, 181, 0.8);
                border: none;
            }

            .nc-enlarge-btn {
                position: absolute;
                top: 16px;
                right: 16px;
                background: rgba(80, 80, 80, 0.5);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
                color: #fff;
                border: none;
                padding: 6px 12px;
                font-size: 10px;
                font-weight: 700;
                letter-spacing: 0.08em;
                border-radius: 4px;
                cursor: pointer;
                transition: background 0.2s;
            }
            .nc-enlarge-btn:hover {
                background: rgba(100, 100, 100, 0.8);
            }

            /* RIGHT: CONTENT */
            .nc-content {
                display: flex;
                flex-direction: column;
                justify-content: center;
                position: relative;
            }

            .nc-tag {
                display: inline-flex;
                padding: 5px 12px;
                background: rgba(0, 229, 181, 0.08);
                border: 1px solid rgba(0, 229, 181, 0.25);
                color: #00e5b5;
                border-radius: 6px;
                font-size: 11px;
                font-weight: 500;
                font-family: SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace;
                margin-bottom: 24px;
                width: fit-content;
                letter-spacing: 0.05em;
            }

            .nc-title {
                font-size: 36px;
                font-weight: 700;
                color: #ffffff;
                margin-bottom: 16px;
                letter-spacing: -0.5px;
                line-height: 1.2;
            }

            .nc-desc {
                font-size: 14px;
                color: #8b8b9e;
                line-height: 1.6;
                margin-bottom: 32px;
            }

            .nc-divider {
                height: 1px;
                background: rgba(255,255,255,0.06);
                border: none;
                margin-bottom: 24px;
                width: 100%;
            }

            /* LIST */
            .nc-list {
                display: flex;
                flex-direction: column;
                gap: 8px;
                max-height: 280px;
                overflow-y: auto;
                padding-right: 10px;
                padding-bottom: 10px;
            }
            .nc-list::-webkit-scrollbar {
                width: 4px;
            }
            .nc-list::-webkit-scrollbar-track {
                background: rgba(255,255,255,0.02);
            }
            .nc-list::-webkit-scrollbar-thumb {
                background: rgba(255,255,255,0.1);
                border-radius: 4px;
            }

            .nc-item {
                padding: 16px 20px;
                border-radius: 10px;
                font-size: 14px;
                color: #6b6b80;
                background: transparent;
                border: 1px solid transparent;
                cursor: pointer;
                display: flex;
                justify-content: space-between;
                align-items: center;
                transition: all 0.2s ease;
                font-weight: 600;
            }

            .nc-item:hover:not(.active) {
                border-color: #3b82f6; /* Hover highlight from image */
                color: #a1a1aa;
            }

            .nc-item.active {
                background: #151515; /* Dark selection match image */
                color: #ffffff;
                border-color: transparent;
            }

            .nc-item.active .nc-dot {
                width: 6px;
                height: 6px;
                border-radius: 50%;
                background: #00e5b5; /* Cyan dot */
                box-shadow: 0 0 6px rgba(0,229,181,0.5);
                display: block;
            }

            .nc-item .nc-dot {
                display: none;
            }

            /* Modal for enlarge */
            .nc-modal {
                position: fixed;
                top: 0; left: 0; right: 0; bottom: 0;
                background: rgba(0,0,0,0.85);
                backdrop-filter: blur(10px);
                -webkit-backdrop-filter: blur(10px);
                z-index: 9999;
                display: flex;
                align-items: center;
                justify-content: center;
                opacity: 0;
                pointer-events: none;
                transition: opacity 0.3s;
            }
            .nc-modal.show {
                opacity: 1;
                pointer-events: auto;
            }
            .nc-modal img {
                max-width: 90%;
                max-height: 85vh;
                border-radius: 12px;
                box-shadow: 0 20px 50px rgba(0,0,0,0.5);
                transform: scale(0.95);
                transition: transform 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
            }
            .nc-modal.show img {
                transform: scale(1);
            }
            .nc-modal-close {
                position: absolute;
                top: 30px;
                right: 30px;
                background: rgba(255,255,255,0.1);
                width: 44px;
                height: 44px;
                border-radius: 50%;
                color: #fff;
                border: none;
                font-size: 24px;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                transition: background 0.2s;
            }
            .nc-modal-close:hover {
                background: rgba(255,255,255,0.2);
            }

            @media (max-width: 900px) {
                .new-certs-container {
                    grid-template-columns: 1fr;
                    gap: 60px;
                }
                .nc-visuals {
                    height: 300px;
                }
                .nc-card {
                    width: 340px;
                    height: 240px;
                }
                .nc-crosshair {
                    display: none;
                }
            }
            @media (max-width: 400px) {
                .nc-card {
                    width: 280px;
                    height: 200px;
                }
            }
        </style>

        <section class="new-certs-section" id="certificates-section">
            <div class="new-certs-container">
                
                <div class="nc-crosshair">
                    <div class="nc-crosshair-circle"></div>
                </div>

                <!-- Left: Image Stack -->
                <div class="nc-visuals" id="nc-visuals">
                    <!-- Cards will be populated here via JS -->
                </div>
                
                <!-- Right: Info & Navigation -->
                <div class="nc-content scroll-reveal">
                    <div class="nc-tag" id="nc-tag">HackerRank Certified</div>
                    <h2 class="nc-title" id="nc-title">SQL (Basic)</h2>
                    <p class="nc-desc" id="nc-desc">Validated core database programming skills through HackerRank assessment, focusing on problem solving, complex queries, and writing efficient SQL code.</p>
                    
                    <hr class="nc-divider" />
                    
                    <div class="nc-list" id="nc-list">
                        <!-- List items will be populated here via JS -->
                    </div>
                </div>
            </div>
            
            <!-- Enlarge Modal -->
            <div class="nc-modal" id="nc-modal">
                <button class="nc-modal-close" id="nc-modal-close">&times;</button>
                <img src="" id="nc-modal-img" alt="Certificate Full" />
            </div>
        </section>

        <!-- Script for Certificate Section Navigation -->
        <script>
            document.addEventListener('DOMContentLoaded', () => {
                const certData = [
                    {
                        title: "Cloud Computing",
                        issuer: "NPTEL",
                        tag: "NPTEL Certified",
                        desc: "Demonstrated strong foundational knowledge of cloud architectures, deployment models, virtualization, and distributed computing through comprehensive coursework provided by IIT Kharagpur.",
                        img: "certificate/Screenshot%202026-03-12%20at%202.25.12%20AM.png"
                    },
                    {
                        title: "Python (Basic)",
                        issuer: "HackerRank",
                        tag: "HackerRank Certified",
                        desc: "Validated core Python programming skills through HackerRank assessment, focusing on problem solving, data structures, and writing efficient, clean code.",
                        img: "certificate/Screenshot%202026-03-12%20at%202.24.56%20AM.png"
                    },
                    {
                        title: "Frontend Developer (React)",
                        issuer: "thingQbator",
                        tag: "Frontend Developer",
                        desc: "Acquired comprehensive skills in React.js, component-driven architecture, and state management, essential for building modern and responsive frontend web applications.",
                        img: "certificate/Screenshot%202026-03-12%20at%202.26.07%20AM.png"
                    },
                    {
                        title: "ChatGPT-4 Prompt Engineering",
                        issuer: "Infosys",
                        tag: "Infosys Springboard",
                        desc: "Learned advanced techniques for crafting effective prompts to interact with large language models, optimizing generative AI outputs for various business use cases.",
                        img: "certificate/Screenshot%202026-03-12%20at%202.25.53%20AM.png"
                    },
                    {
                        title: "21st Century Workplace",
                        issuer: "Coursera",
                        tag: "Coursera Certified",
                        desc: "Developed essential communication, collaboration, and critical thinking skills required to succeed in modern, fast-paced corporate environments.",
                        img: "certificate/Screenshot%202026-03-12%20at%202.25.27%20AM.png"
                    }
                ];

                let currentActiveCert = 1; // Start with Python (Basic)

                const visualsContainer = document.getElementById('nc-visuals');
                const listContainer = document.getElementById('nc-list');
                const tagEl = document.getElementById('nc-tag');
                const titleEl = document.getElementById('nc-title');
                const descEl = document.getElementById('nc-desc');
                
                const modal = document.getElementById('nc-modal');
                const modalImg = document.getElementById('nc-modal-img');
                const modalClose = document.getElementById('nc-modal-close');

                function renderCerts() {
                    // Update Text Details
                    const activeCert = certData[currentActiveCert];
                    tagEl.textContent = activeCert.tag;
                    titleEl.textContent = activeCert.title;
                    descEl.textContent = activeCert.desc;

                    // Update Right List
                    listContainer.innerHTML = certData.map((cert, index) => {
                        const isActive = index === currentActiveCert;
                        return \`
                            <div class="nc-item \${isActive ? 'active' : ''}" data-index="\${index}">
                                \${cert.title}
                                <span class="nc-dot"></span>
                            </div>
                        \`;
                    }).join('');

                    // Re-bind click events for list items
                    document.querySelectorAll('.nc-item').forEach(item => {
                        item.addEventListener('click', (e) => {
                            currentActiveCert = parseInt(e.currentTarget.getAttribute('data-index'));
                            renderCerts();
                        });
                    });

                    // Update Visual Stack
                    let visualsHTML = '';
                    const total = certData.length;

                    // Calculate indexes for background cards
                    const bg2Index = (currentActiveCert - 1 + total) % total; // Left background
                    const bg1Index = (currentActiveCert + 1) % total;     // Right background

                    // We render them in specific z-index order (lowest to highest)
                    visualsHTML += \`
                        <div class="nc-card bg-2">
                            <img src="\${certData[bg2Index].img}" alt="" loading="lazy" />
                        </div>
                    \`;

                    visualsHTML += \`
                        <div class="nc-card bg-1">
                            <img src="\${certData[bg1Index].img}" alt="" loading="lazy" />
                        </div>
                    \`;

                    visualsHTML += \`
                        <div class="nc-card active">
                            <img src="\${activeCert.img}" alt="\${activeCert.title}" />
                            <button class="nc-enlarge-btn" onclick="document.getElementById('nc-modal-img').src='\${activeCert.img}'; document.getElementById('nc-modal').classList.add('show');">ENLARGE</button>
                        </div>
                    \`;

                    visualsContainer.innerHTML = visualsHTML;
                }

                // Modal interactions
                modalClose.addEventListener('click', () => {
                    modal.classList.remove('show');
                });
                modal.addEventListener('click', (e) => {
                    if (e.target === modal) {
                        modal.classList.remove('show');
                    }
                });

                // Initial render
                renderCerts();
            });
        </script>
"""

new_text = text[:start_idx] + replacement_string + "\n        " + text[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Success")
