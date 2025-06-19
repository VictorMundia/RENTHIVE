import React from "react";
import { useNavigate } from "react-router-dom";
// If you use a UI library, import the Button from there. Otherwise, use a simple button.
// import { Button } from "@/components/ui/button";

const Button = ({ children, ...props }) => (
  <button className="px-4 py-2 rounded bg-primary text-white hover:bg-primary/80 transition" {...props}>{children}</button>
);

// HexagonIcon component
const HexagonIcon = ({ className }) => (
  <svg
    className={`inline-block h-6 w-6 ${className || ''}`}
    fill="currentColor"
    viewBox="0 0 24 24"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M12 .587l10.392 6v12L12 23.413L1.608 18.587v-12L12 .587zm0 2.05L3.65 8.05v8l8.35 4.903 8.35-4.903v-8L12 2.637z" />
  </svg>
);

export default function Landing() {
  const navigate = useNavigate();
  return (
    <div className="flex flex-col min-h-screen bg-background text-foreground">
      {/* Header */}
      <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="container flex h-14 max-w-screen-2xl items-center">
          <div className="mr-4 hidden md:flex">
            <a className="mr-6 flex items-center space-x-2" href="/">
              {/* <HexagonIcon className="text-primary" /> */}
              <span className="hidden font-bold sm:inline-block text-xl">
                RentHive
              </span>
            </a>
            <nav className="flex items-center gap-4 text-sm lg:gap-6">
              {/* Navigation links can be added here */}
            </nav>
          </div>
          <div className="flex flex-1 items-center justify-end space-x-2">
            <Button onClick={() => navigate("/login")}>Login</Button>
            <Button onClick={() => navigate("/signup")}>Sign Up</Button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-grow">
        {/* Hero Section */}
        <section className="py-12 md:py-24 lg:py-32 bg-secondary/50">
          <div className="container mx-auto px-4 text-center">
            <h1 className="text-4xl font-bold tracking-tight sm:text-5xl md:text-6xl">
              Manage Your Rentals, <span className="text-primary">Seamlessly</span>.
            </h1>
            <p className="mt-6 max-w-2xl mx-auto text-lg text-muted-foreground sm:text-xl md:text-2xl">
              RentHive simplifies rental management for small property owners in Kenya.
              Automate reminders, track maintenance, and communicate effortlessly.
            </p>
            <div className="mt-10 flex justify-center gap-x-4">
              <Button onClick={() => navigate("/signup")}>Get Started</Button>
              <Button variant="outline">Learn More</Button>
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section id="features" className="py-12 md:py-24 lg:py-32">
          <div className="container mx-auto px-4">
            <div className="text-center mb-12">
              <h2 className="text-3xl font-bold tracking-tight sm:text-4xl md:text-5xl">
                Why Choose <span className="text-primary">RentHive</span>?
              </h2>
              <p className="mt-4 max-w-xl mx-auto text-lg text-muted-foreground">
                Everything you need to manage your properties efficiently.
              </p>
            </div>
            <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
              {/* Feature 1 */}
              <div className="p-6 bg-card border rounded-lg shadow-sm hover:shadow-md transition-shadow">
                <div className="flex items-center justify-center mb-4 h-16 w-16 rounded-lg bg-primary/10 text-primary">
                  <HexagonIcon className="h-8 w-8" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Rent Reminders</h3>
                <p className="text-muted-foreground">
                  Automated rent reminders for tenants, ensuring timely payments.
                </p>
              </div>
              {/* Feature 2 */}
              <div className="p-6 bg-card border rounded-lg shadow-sm hover:shadow-md transition-shadow">
                <div className="flex items-center justify-center mb-4 h-16 w-16 rounded-lg bg-primary/10 text-primary">
                  <HexagonIcon className="h-8 w-8" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Maintenance Requests</h3>
                <p className="text-muted-foreground">
                  Streamlined maintenance requests and tracking for quick resolutions.
                </p>
              </div>
              {/* Feature 3 */}
              <div className="p-6 bg-card border rounded-lg shadow-sm hover:shadow-md transition-shadow">
                <div className="flex items-center justify-center mb-4 h-16 w-16 rounded-lg bg-primary/10 text-primary">
                  <HexagonIcon className="h-8 w-8" />
                </div>
                <h3 className="text-xl font-semibold mb-2">Easy Communication</h3>
                <p className="text-muted-foreground">
                  In-app messenger and WhatsApp integration for seamless landlord-tenant communication.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Benefits Section */}
        <section id="benefits" className="py-12 md:py-24 lg:py-32 bg-secondary/50">
          <div className="container mx-auto px-4 text-center">
            <h2 className="text-3xl font-bold tracking-tight sm:text-4xl md:text-5xl">
              Benefits for <span className="text-primary">Everyone</span>
            </h2>
            <p className="mt-4 max-w-xl mx-auto text-lg text-muted-foreground mb-12">
              RentHive is designed to make life easier for both property owners and tenants.
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 text-left">
              {/* Property Owners benefits */}
              <div className="p-6 bg-card border rounded-lg shadow-sm">
                <h3 className="text-xl font-semibold mb-2 text-primary">For Property Owners</h3>
                <ul className="list-disc list-inside space-y-1 text-muted-foreground">
                  <li>Save time with automated tasks.</li>
                  <li>Improve tenant communication.</li>
                  <li>Keep track of finances and maintenance easily.</li>
                  <li>Reduce vacancies with a happy tenant base.</li>
                </ul>
              </div>
              {/* Tenants benefits */}
              <div className="p-6 bg-card border rounded-lg shadow-sm">
                <h3 className="text-xl font-semibold mb-2 text-primary">For Tenants</h3>
                <ul className="list-disc list-inside space-y-1 text-muted-foreground">
                  <li>Easy rent payments and reminders.</li>
                  <li>Quickly report and track maintenance issues.</li>
                  <li>Clear communication with your landlord.</li>
                  <li>Access to important lease documents.</li>
                </ul>
              </div>
            </div>
          </div>
        </section>

        {/* Call to Action */}
        <section className="py-12 md:py-24 lg:py-32">
          <div className="container mx-auto px-4 text-center">
            <h2 className="text-3xl font-bold tracking-tight sm:text-4xl md:text-5xl">
              Ready to <span className="text-primary">Simplify</span> Your Rentals?
            </h2>
            <p className="mt-4 max-w-xl mx-auto text-lg text-muted-foreground">
              Join RentHive today and experience the future of rental management.
            </p>
            <div className="mt-10">
              <Button onClick={() => navigate("/signup")}>Sign Up Now - It's Free!</Button>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="py-8 border-t">
        <div className="container mx-auto px-4 text-center text-muted-foreground">
          <p>&copy; {new Date().getFullYear()} RentHive. All rights reserved.</p>
          <p className="text-sm">Empowering Property Management in Kenya.</p>
        </div>
      </footer>
    </div>
  );
}
