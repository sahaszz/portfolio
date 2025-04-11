import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Mail, Phone, Download } from "lucide-react";
import { motion } from "framer-motion";
import Image from "next/image";

export default function Portfolio() {
  return (
    <div className="min-h-screen bg-white text-gray-800 font-sans">
      {/* Navbar */}
      <nav className="sticky top-0 z-50 bg-white border-b shadow-sm py-4 px-8 flex justify-between items-center">
        <h1 className="text-2xl font-bold text-indigo-700">Sudipta Saha</h1>
        <div className="space-x-4 text-sm font-medium">
          <a href="#about" className="hover:text-indigo-600">About</a>
          <a href="#experience" className="hover:text-indigo-600">Experience</a>
          <a href="#skills" className="hover:text-indigo-600">Skills</a>
          <a href="#education" className="hover:text-indigo-600">Education</a>
          <a href="#contact" className="hover:text-indigo-600">Contact</a>
        </div>
      </nav>

      {/* Hero Section */}
      <header className="bg-gradient-to-br from-indigo-50 to-purple-100 text-center py-20 px-4">
        <motion.div 
          initial={{ opacity: 0, y: -30 }} 
          animate={{ opacity: 1, y: 0 }} 
          transition={{ duration: 0.6 }}>
          <h2 className="text-5xl font-extrabold text-indigo-800 mb-3">Sudipta Saha</h2>
          <p className="text-xl text-gray-700 mb-2">IT Coordinator | Full-Stack Developer</p>
          <p className="text-sm text-gray-600">Kolkata, India</p>
          <div className="mt-6 flex justify-center gap-4">
            <a href="mailto:sudipta.saha177@gmail.com" className="text-indigo-600 hover:underline flex items-center gap-2">
              <Mail size={18} /> sudipta.saha177@gmail.com
            </a>
            <a href="tel:+919674414640" className="text-indigo-600 hover:underline flex items-center gap-2">
              <Phone size={18} /> +91 96744 14640
            </a>
          </div>
          <div className="mt-6">
            <Button variant="default" size="lg">
              <Download className="mr-2" size={18} /> Download Resume
            </Button>
          </div>
        </motion.div>
      </header>

      {/* About Section */}
      <section id="about" className="py-16 px-4 max-w-4xl mx-auto text-center">
        <h2 className="text-3xl font-bold text-indigo-800 mb-6">About Me</h2>
        <p className="text-gray-700 leading-relaxed text-lg">
          Passionate about solving complex problems through elegant code and scalable solutions. With over 8 years of experience in software development and IT infrastructure, I enjoy turning ideas into reality.
        </p>
      </section>

      {/* Experience Section */}
      <section id="experience" className="bg-gray-50 py-16 px-4">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-3xl font-bold text-indigo-800 mb-8 text-center">Work Experience</h2>
          <div className="grid gap-8 md:grid-cols-2">
            {[
              { org: "Ashok Laboratory Clinical Testing Centre Pvt Ltd", role: "IT Coordinator", period: "Feb 2024 - Present" },
              { org: "HCL Technologies Pvt Ltd", role: "Senior Technical Specialist", period: "May 2017 – March 2023" },
              { org: "Encoders", role: "PHP Developer", period: "Jun 2016 - Jan 2017" },
              { org: "Elphill Technology", role: "PHP Developer", period: "Jun 2015 - May 2016" }
            ].map((item, idx) => (
              <motion.div 
                key={idx} 
                initial={{ opacity: 0, y: 20 }} 
                whileInView={{ opacity: 1, y: 0 }} 
                transition={{ duration: 0.4, delay: idx * 0.1 }}>
                <Card className="shadow-lg transition-transform hover:scale-[1.02]">
                  <CardContent className="p-6">
                    <h3 className="text-xl font-semibold text-indigo-700 mb-1">{item.org}</h3>
                    <p className="text-md text-gray-600 font-medium">{item.role}</p>
                    <p className="text-sm text-gray-500 italic">{item.period}</p>
                  </CardContent>
                </Card>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <section id="skills" className="py-16 px-4 text-center">
        <h2 className="text-3xl font-bold text-indigo-800 mb-6">Skills</h2>
        <ul className="grid grid-cols-2 md:grid-cols-3 gap-4 text-lg font-semibold text-indigo-700">
          <li>🧠 C#</li>
          <li>🧠 .NET / ASP.NET / ADO.NET</li>
          <li>🧠 PHP</li>
          <li>🧠 JavaScript & jQuery</li>
          <li>🧠 PowerShell</li>
          <li>🧠 MySQL & Oracle</li>
        </ul>
      </section>

      {/* Education Section */}
      <section id="education" className="bg-gray-50 py-16 px-4 text-center">
        <h2 className="text-3xl font-bold text-indigo-800 mb-6">Education</h2>
        <ul className="text-gray-700 leading-loose text-lg">
          <li>🎓 <strong>B.Tech</strong> in Computer Science – Future Institute of Engineering & Management (74.2%)</li>
          <li>🎓 <strong>Diploma</strong> in Computer Science – Kingstone Polytechnic (73.3%)</li>
        </ul>
      </section>

      {/* Contact Section */}
      <section id="contact" className="py-16 px-4 text-center">
        <h2 className="text-3xl font-bold text-indigo-800 mb-6">Contact</h2>
        <p className="text-lg text-gray-700 mb-4">I'd love to hear from you! Feel free to reach out.</p>
        <div className="flex justify-center gap-6 text-indigo-600">
          <a href="mailto:sudipta.saha177@gmail.com" className="flex items-center gap-2 hover:underline">
            <Mail size={18} /> sudipta.saha177@gmail.com
          </a>
          <a href="tel:+919674414640" className="flex items-center gap-2 hover:underline">
            <Phone size={18} /> +91 96744 14640
          </a>
        </div>
      </section>

      {/* Footer */}
      <footer className="text-center text-sm text-gray-500 mt-10 border-t pt-6">
        &copy; {new Date().getFullYear()} Sudipta Saha. All rights reserved.
      </footer>
    </div>
  );
}
