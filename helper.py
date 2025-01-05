import os
import subprocess


# Package management

def get_dnf_history():
    output = subprocess.run(['dnf', 'history'], capture_output=True, text=True)
    return output.stdout


# Network information


def get_ip_address():
    output = subprocess.run(['ip', 'addr'], capture_output=True, text=True)
    return output.stdout


def get_routes():
    output = subprocess.run(['ip', 'route'], capture_output=True, text=True)
    return output.stdout



def get_listening_ports():
    output = subprocess.run(['ss', '-tuln'], capture_output=True, text=True)
    return output.stdout


# OS information
def get_kernel_version():
    return os.uname().release

def get_uptime():
    return os.popen('uptime').read()

def get_boot_time_blame():
    output = subprocess.run(['systemd-analyze', 'blame'], capture_output=True, text=True)
    return output.stdout

def get_journal_since_last_boot():
    # Get the journal logs since the last boot
    output = subprocess.run(['journalctl', '-b'], capture_output=True, text=True)
    return output.stdout

# Services
def get_failed_services():
    output = subprocess.run(['systemctl', '--failed'], capture_output=True, text=True)
    return output.stdout

def get_running_services():
    output = subprocess.run(['systemctl', 'list-units', '--type=service', '--state=running'], capture_output=True, text=True)
    return output.stdout

def get_services_by_memory():
    # Use ps to list processes, sort by memory, and filter for services
    output = subprocess.run(['ps', 'aux', '--sort=-%mem'], capture_output=True, text=True)
    return output.stdout

def get_disabled_services():
    # List all unit files, filter by services that are disabled
    output = subprocess.run(['systemctl', 'list-unit-files', '--type=service', '--state=disabled'], capture_output=True, text=True)
    return output.stdout