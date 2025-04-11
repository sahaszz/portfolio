<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sudipta Saha - Professional Portfolio</title>
    <style>
        /* Global Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
        }
        
        .container {
            max-width: 1140px;
            margin: 0 auto;
            padding: 0 15px;
        }
        
        /* Header */
        header {
            background-color: #2c3e50;
            color: #fff;
            padding: 60px 0 40px;
        }
        
        .header-content {
            text-align: center;
        }
        
        .header-content h1 {
            font-size: 2.8rem;
            margin-bottom: 10px;
        }
        
        .header-content h2 {
            font-size: 1.8rem;
            font-weight: 400;
            margin-bottom: 20px;
            color: #ecf0f1;
        }
        
        .contact-info {
            margin-top: 20px;
            font-size: 1.1rem;
        }
        
        .contact-info a {
            color: #3498db;
            text-decoration: none;
        }
        
        .contact-info a:hover {
            text-decoration: underline;
        }
        
        /* Section Styling */
        section {
            padding: 60px 0;
        }
        
        section:nth-child(even) {
            background-color: #fff;
        }
        
        .section-title {
            text-align: center;
            font-size: 2rem;
            margin-bottom: 40px;
            position: relative;
        }
        
        .section-title:after {
            content: '';
            display: block;
            width: 80px;
            height: 3px;
            background-color: #3498db;
            margin: 10px auto 0;
        }
        
        /* Summary Section */
        .summary {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
            font-size: 1.2rem;
        }
        
        /* Skills Section */
        .skills {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            max-width: 900px;
            margin: 0 auto;
        }
        
        .skill-category {
            width: 48%;
            margin-bottom: 30px;
        }
        
        .skill-category h3 {
            margin-bottom: 15px;
            color: #2c3e50;
        }
        
        .skill-list {
            margin-left: 20px;
        }
        
        /* Experience Section */
        .experience-item {
            margin-bottom: 40px;
        }
        
        .job-title {
            font-size: 1.4rem;
            color: #2c3e50;
            margin-bottom: 5px;
        }
        
        .company {
            font-size: 1.2rem;
            margin-bottom: 5px;
        }
        
        .duration {
            font-style: italic;
            color: #7f8c8d;
            margin-bottom: 15px;
        }
        
        .project {
            margin: 20px 0;
            padding: 15px;
            background-color: #f8f9fa;
            border-left: 4px solid #3498db;
        }
        
        .project h4 {
            color: #2c3e50;
            margin-bottom: 10px;
        }
        
        /* Education Section */
        .education-item {
            margin-bottom: 20px;
        }
        
        .degree {
            font-weight: bold;
        }
        
        /* Portfolio Section */
        .portfolio {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 30px;
        }
        
        .portfolio-item {
            background-color: #fff;
            border-radius: 5px;
            overflow: hidden;
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s;
        }
        
        .portfolio-item:hover {
            transform: translateY(-5px);
        }
        
        .portfolio-img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        
        .portfolio-info {
            padding: 20px;
        }
        
        .portfolio-info h3 {
            margin-bottom: 10px;
            color: #2c3e50;
        }
        
        .tech-stack {
            font-style: italic;
            color: #7f8c8d;
            margin-top: 10px;
        }
        
        /* Certifications & Interests */
        .cert-interests {
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
        }
        
        .certifications, .interests {
            width: 48%;
        }
        
        .cert-interests h3 {
            margin-bottom: 15px;
            color: #2c3e50;
        }
        
        .cert-interests ul {
            margin-left: 20px;
        }
        
        /* Footer */
        footer {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 30px 0;
            text-align: center;
        }
        
        /* Media Queries */
        @media (max-width: 768px) {
            .skill-category, .certifications, .interests {
                width: 100%;
            }
            
            .portfolio {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <div class="container header-content">
            <h1>Sudipta Saha</h1>
            <h2>Senior Software Developer</h2>
            <div class="contact-info">
                <p>Email: <a href="mailto:sudipta.saha177@gmail.com">sudipta.saha177@gmail.com</a> | Phone: +91 9674414640 | Kolkata, India</p>
                <p>
                    <a href="https://linkedin.com/in/sudiptasaha" target="_blank">LinkedIn</a> | 
                    <a href="https://github.com/sudiptasaha" target="_blank">GitHub</a>
                </p>
            </div>
        </div>
    </header>

    <!-- Professional Summary -->
    <section>
        <div class="container">
            <h2 class="section-title">Professional Summary</h2>
            <div class="summary">
                <p>Versatile Software Developer with 8+ years of experience in application development and database solutions. Skilled in building efficient enterprise applications using C#, .NET, ASP.NET, ADO.NET, PHP, JavaScript, jQuery, and PowerShell. Proficient in working with relational databases including MS SQL Server, MySQL, and Oracle.</p>
            </div>
        </div>
    </section>

    <!-- Technical Skills -->
    <section>
        <div class="container">
            <h2 class="section-title">Technical Skills</h2>
            <div class="skills">
                <div class="skill-category">
                    <h3>Programming Languages</h3>
                    <ul class="skill-list">
                        <li>C#</li>
                        <li>PHP</li>
                        <li>JavaScript</li>
                    </ul>
                </div>
                <div class="skill-category">
                    <h3>Frameworks & Libraries</h3>
                    <ul class="skill-list">
                        <li>.NET</li>
                        <li>ASP.NET</li>
                        <li>ADO.NET</li>
                        <li>MVC</li>
                        <li>jQuery</li>
                        <li>Ajax</li>
                    </ul>
                </div>
                <div class="skill-category">
                    <h3>Scripting</h3>
                    <ul class="skill-list">
                        <li>PowerShell</li>
                    </ul>
                </div>
                <div class="skill-category">
                    <h3>Databases</h3>
                    <ul class="skill-list">
                        <li>Oracle</li>
                        <li>MySQL</li>
                        <li>MS SQL Server</li>
                    </ul>
                </div>
                <div class="skill-category">
                    <h3>Others</h3>
                    <ul class="skill-list">
                        <li>RESTful API development</li>
                        <li>Version control systems</li>
                    </ul>
                </div>
                <div class="skill-category">
                    <h3>Languages</h3>
                    <ul class="skill-list">
                        <li>English</li>
                        <li>Bengali</li>
                        <li>Hindi</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Professional Experience -->
    <section>
        <div class="container">
            <h2 class="section-title">Professional Experience</h2>

            <div class="experience-item">
                <h3 class="job-title">IT Coordinator</h3>
                <p class="company">Ashok Laboratory Clinical Testing Centre Pvt Ltd</p>
                <p class="duration">February 2024 - Present</p>
                <ul>
                    <li>Managing IT infrastructure and database solutions</li>
                    <li>Developing and maintaining internal applications and tools</li>
                    <li>Ensuring seamless operation of laboratory information systems</li>
                </ul>
            </div>

            <div class="experience-item">
                <h3 class="job-title">Senior Technical Specialist</h3>
                <p class="company">HCL Technologies Pvt Ltd</p>
                <p class="duration">May 2017 - March 2023</p>

                <div class="project">
                    <h4>Global Order Tool</h4>
                    <p>Developed a workflow management system for global deployment of multi-component products. Implemented support for Windows/UNIX Services, Netcom, and Storage components.</p>
                    <p class="tech-stack">Technologies: C#, MVC architecture, MySQL database</p>
                </div>

                <div class="project">
                    <h4>Event Management Portal</h4>
                    <p>Created a comprehensive reporting tool generating daily and monthly reports for iSeries, mainframe, Unix, Network telecom, and Open Storage systems.</p>
                    <p class="tech-stack">Technologies: C#, MVC architecture, JavaScript, jQuery, Oracle database</p>
                </div>

                <div class="project">
                    <h4>MAID (Mainframe Application Information and Documentation)</h4>
                    <p>Engineered a document management system for mainframe applications. Developed PowerShell scripts for file processing and service management. Implemented continuous service monitoring and automated file processing.</p>
                    <p class="tech-stack">Technologies: C#, PowerShell scripts, MySQL database</p>
                </div>

                <div class="project">
                    <h4>HID (Hosting Information Database)</h4>
                    <p>Created a management interface for .NET Hosting Platform. Implemented customer information storage, CMDB integration, deployment mechanisms, and comprehensive logging systems.</p>
                    <p class="tech-stack">Technologies: C#, MVC architecture, JavaScript, jQuery, MySQL database</p>
                </div>

                <div class="project">
                    <h4>MOMA/EMMA</h4>
                    <p>Built an alert generation system based on system events (MOMA). Developed a task monitoring and management system for application teams (EMMA).</p>
                    <p class="tech-stack">Technologies: PHP, MVC architecture, JavaScript, jQuery, Oracle database</p>
                </div>

                <div class="project">
                    <h4>DICA (Documentation of Interzone Communication for Applications)</h4>
                    <p>Developed a system for managing network communication rules and firewall settings. Implemented complex workflows and role-based access control.</p>
                    <p class="tech-stack">Technologies: C#, MVC architecture, JavaScript, jQuery, MySQL database</p>
                </div>
            </div>

            <div class="experience-item">
                <h3 class="job-title">PHP Developer</h3>
                <p class="company">Encoders</p>
                <p class="duration">June 2016 - January 2017</p>

                <div class="project">
                    <h4>Osheaherbals</h4>
                    <p>Developed an e-commerce website for beauty and personal care products.</p>
                    <p class="tech-stack">Technologies: PHP, JavaScript, jQuery, Ajax</p>
                </div>

                <div class="project">
                    <h4>Rubanshop</h4>
                    <p>Created an online bookstore with nationwide delivery capabilities.</p>
                    <p class="tech-stack">Technologies: PHP, JavaScript, jQuery, Ajax</p>
                </div>
            </div>

            <div class="experience-item">
                <h3 class="job-title">PHP Developer</h3>
                <p class="company">Elphill Technology</p>
                <p class="duration">June 2015 - May 2016</p>

                <div class="project">
                    <h4>Adhoards</h4>
                    <p>Contributed to a leading classifieds platform for buying, selling goods, and job searching.</p>
                    <p class="tech-stack">Technologies: PHP, MVC structure, JavaScript, jQuery, Ajax</p>
                </div>
            </div>

            <div class="experience-item">
                <h3 class="job-title">PHP Developer</h3>
                <p class="company">ABCDEL</p>
                <p class="duration">December 2014 - May 2015</p>
                <p>Developed web applications using PHP and related technologies.</p>
            </div>
        </div>
    </section>

    <!-- Education -->
    <section>
        <div class="container">
            <h2 class="section-title">Education</h2>
            
            <div class="education-item">
                <p><span class="degree">Bachelor of Technology</span><br>
                Future Institute of Engineering & Management<br>
                Score: 74.2%</p>
            </div>
            
            <div class="education-item">
                <p><span class="degree">Diploma in Computer Science</span><br>
                Kingstone Polytechnic<br>
                Score: 73.3%</p>
            </div>
            
            <div class="education-item">
                <p><span class="degree">12th Standard</span><br>
                Kamala Chatterjee School<br>
                Score: 60.3%</p>
            </div>
            
            <div class="education-item">
                <p><span class="degree">10th Standard</span><br>
                Beltala Girls School<br>
                Score: 71%</p>
            </div>
        </div>
    </section>

    <!-- Project Portfolio -->
    <section>
        <div class="container">
            <h2 class="section-title">Project Portfolio</h2>
            
            <div class="portfolio">
                <div class="portfolio-item">
                    <img src="https://via.placeholder.com/800x400?text=Global+Order+Tool" alt="Global Order Tool" class="portfolio-img">
                    <div class="portfolio-info">
                        <h3>Global Order Tool</h3>
                        <p>A workflow management system supporting global deployment of multi-component products, ensuring high-quality and efficient deployments through coordinated team collaboration.</p>
                        <p class="tech-stack">Technologies: C#, MVC, MySQL</p>
                    </div>
                </div>
                
                <div class="portfolio-item">
                    <img src="https://via.placeholder.com/800x400?text=Event+Management+Portal" alt="Event Management Portal" class="portfolio-img">
                    <div class="portfolio-info">
                        <h3>Event Management Portal</h3>
                        <p>A comprehensive reporting system generating daily and monthly tracking reports for various enterprise systems including mainframe, Unix, and Network telecom.</p>
                        <p class="tech-stack">Technologies: C#, MVC, JavaScript, jQuery, Oracle</p>
                    </div>
                </div>
                
                <div class="portfolio-item">
                    <img src="https://via.placeholder.com/800x400?text=Osheaherbals+E-commerce" alt="Osheaherbals E-commerce" class="portfolio-img">
                    <div class="portfolio-info">
                        <h3>Osheaherbals E-commerce</h3>
                        <p>A complete e-commerce solution for beauty and personal care products with product catalog, shopping cart, and secure payment processing.</p>
                        <p class="tech-stack">Technologies: PHP, JavaScript, jQuery, Ajax</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Certifications & Interests -->
    <section>
        <div class="container">
            <h2 class="section-title">Additional Information</h2>
            
            <div class="cert-interests">
                <div class="certifications">
                    <h3>Certifications</h3>
                    <ul>
                        <li>Microsoft Certified: Azure Developer Associate</li>
                        <li>Oracle Certified Professional, Java SE Programmer</li>
                    </ul>
                </div>
                
                <div class="interests">
                    <h3>Professional Interests</h3>
                    <ul>
                        <li>Cloud-native application development</li>
                        <li>DevOps and CI/CD pipelines</li>
                        <li>Microservices architecture</li>
                        <li>Database optimization and performance tuning</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <p>&copy; 2025 Sudipta Saha. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
