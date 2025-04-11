import { Mail, Phone } from "lucide-react";

export default function Portfolio() {
  return (
    <div className="min-h-screen bg-white text-gray-800 font-sans">
      {/* Header */}
      <header className="bg-gray-100 py-8 text-center">
        <h1 className="text-4xl font-bold">Sudipta Saha</h1>
        <p className="mt-2 text-lg">IT Coordinator | Full Stack Developer</p>
        <p className="mt-1 text-sm text-gray-600">Kolkata, India</p>
        <div className="mt-4 flex justify-center gap-4">
          <a href="mailto:sudipta.saha177@gmail.com" className="text-blue-600 hover:underline flex items-center gap-1">
            <Mail size={16} /> Email
          </a>
          <a href="tel:+919674414640" className="text-blue-600 hover:underline flex items-center gap-1">
            <Phone size={16} /> Call
          </a>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-3xl mx-auto p-6">
        {/* About Section */}
        <section id="about" className="my-8">
          <h2 className="text-2xl font-semibold mb-4">About Me</h2>
          <p>
            I am passionate about solving complex problems through elegant code and scalable solutions. With over 8 years of experience in software development and IT infrastructure, I enjoy turning ideas into reality.
          </p>
        </section>

        {/* Experience Section */}
        <section id="experience" className="my-8">
          <h2 className="text-2xl font-semibold mb-4">Work Experience</h2>
          <ul className="space-y-4">
            <li>
              <h3 className="font-bold">Ashok Laboratory Clinical Testing Centre Pvt Ltd</h3>
              <p>IT Coordinator | Feb 2024 - Present</p>
            </li>
            <li>
              <h3 className="font-bold">HCL Technologies Pvt Ltd</h3>
              <p>Senior Technical Specialist | May 2017 to March 2023</p>
            </li>
            <li>
              <h3 className="font-bold">Encoders</h3>
              <p>PHP Developer | Jun 2016 to Jan 2017</p>
            </li>
            <li>
              <h3 className="font-bold">Elphill Technology</h3>
              <p>PHP Developer | Jun 2015 to May 2016</p>
            </li>
          </ul>
        </section>

        {/* Skills Section */}
        <section id="skills" className="my-8">
          <h2 className="text-2xl font-semibold mb-4">Skills</h2>
          <ul className="list-disc ml-6">
            <li>C#</li>
            <li>.NET / ASP.NET / ADO.NET</li>
            <li>PHP</li>
            <li>JavaScript & jQuery</li>
            <li>PowerShell</li>
            <li>MySQL & Oracle</li>
          </ul>
        </section>

        {/* Education Section */}
        <section id="education" className="my-8">
          <h2 className="text-2xl font-semibold mb-4">Education</h2>
          <ul className="list-disc ml-6">
            <li>B.Tech in Computer Science  Future Institute of Engineering & Management (74.2%)</li>
            <li>Diploma in Computer Science  Kingstone Polytechnic (73.3%)</li>
          </ul>
        </section>

        {/* Contact Section */}
        <section id="contact" className="my-8 text-center">
          <h2 className="text-2xl font-semibold mb-4">Contact</h2>
          <p>If you would like to get in touch, please send an email or give me a call.</p>
          <div className="mt-4 flex justify-center gap-4">
            <a href="mailto:sudipta.saha177@gmail.com" className="text-blue-600 hover:underline flex items-center gap-1">
              <Mail size={16} /> Email
            </a>
            <a href="tel:+919674414640" className="text-blue-600 hover:underline flex items-center gap-1">
              <Phone size={16} /> Call
            </a>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="bg-gray-100 py-4 text-center text-sm text-gray-600">
        &copy; {new Date().getFullYear()} Sudipta Saha. All rights reserved.
      </footer>
    </div>
  );
}
