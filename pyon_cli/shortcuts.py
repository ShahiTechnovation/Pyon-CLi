"""Create shortcut commands for easier Pyon CLI usage."""

import os
from pathlib import Path
from rich.console import Console

console = Console()


def create_shortcuts():
    """Create batch file shortcuts for common Pyon CLI commands."""
    
    shortcuts = {
        "pyon.bat": "python -m pyon_cli.cli %*",
        "compile.bat": "python -m pyon_cli.cli compile",
        "deploy.bat": "python -m pyon_cli.cli deploy %1",
        "info.bat": "python -m pyon_cli.cli info %1"
    }
    
    created_files = []
    
    for filename, command in shortcuts.items():
        try:
            with open(filename, "w") as f:
                f.write(f"@echo off\n{command}\n")
            created_files.append(filename)
        except Exception as e:
            console.print(f"[red]Failed to create {filename}: {e}[/red]")
    
    if created_files:
        console.print("[green]✅ Shortcut commands created:[/green]")
        for filename in created_files:
            console.print(f"  📄 {filename}")
        
        console.print("\n[cyan]Usage examples:[/cyan]")
        console.print("  .\\pyon.bat compile")
        console.print("  .\\deploy.bat MyContract")
        console.print("  .\\info.bat StakeToken")
    
    return created_files


def setup_environment():
    """Set up development environment with shortcuts and checks."""
    
    console.print("[blue]Setting up Pyon CLI development environment...[/blue]")
    
    # Create shortcuts
    shortcuts = create_shortcuts()
    
    # Check environment
    checks = []
    
    # Check if in project directory
    if Path("pyon_config.json").exists():
        checks.append("✅ Project configuration found")
    else:
        checks.append("⚠️ Not in Pyon CLI project directory")
    
    # Check contracts directory
    if Path("contracts").exists():
        contract_files = list(Path("contracts").glob("*.py"))
        checks.append(f"✅ Contracts directory ({len(contract_files)} Python files)")
    else:
        checks.append("⚠️ No contracts directory found")
    
    # Check private key
    if os.getenv('PRIVATE_KEY'):
        checks.append("✅ Private key environment variable set")
    else:
        checks.append("⚠️ PRIVATE_KEY environment variable not set")
    
    console.print("\n[cyan]Environment Status:[/cyan]")
    for check in checks:
        console.print(f"  {check}")
    
    return len(shortcuts) > 0


if __name__ == "__main__":
    setup_environment()
