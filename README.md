# Pyon CLI - Polygon Smart Contract CLI

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Pyon CLI** is a production-ready CLI tool for deploying Solidity and Python smart contracts to Polygon. It features a unique **Python-to-EVM transpiler** that allows you to write smart contracts in Python and deploy them directly to the blockchain.

## 🚀 Features

- **Python Smart Contracts**: Write smart contracts in Python and transpile them to EVM bytecode
- **Solidity Support**: Full support for Solidity contract compilation and deployment
- **Multi-Network**: Deploy to Polygon Amoy testnet or mainnet
- **Secure Wallet Management**: Encrypted keystore with PBKDF2 encryption
- **Gas Estimation**: Accurate gas estimation before deployment
- **Rich CLI Interface**: Beautiful command-line interface with progress indicators
- **Deployment Tracking**: Automatic tracking of deployed contracts

## 📦 Installation

### Using pip

```bash
pip install -e .
```

### Using pip with requirements.txt

```bash
pip install -r requirements.txt
pip install -e .
```

### Development Installation

```bash
pip install -e ".[dev]"
```

## 🔧 Quick Start

### 1. Initialize a New Project

```bash
python -m pyon_cli.cli init my-project
cd my-project
```

This creates a new project with:
- Sample Python and Solidity contracts
- Default configuration file
- Deployment scripts

### 2. Create a Wallet

```bash
pyon-cli wallet new
```

This will:
- Generate a new encrypted wallet
- Save it as `pyon_key.json`
- Display your wallet address

**⚠️ Important**: Fund your wallet with MATIC before deploying contracts!

### 3. Compile Contracts

```bash
pyon-cli compile
```

This compiles both Python and Solidity contracts in the `contracts/` directory.

### 4. Deploy Contracts

```bash
# Deploy to Amoy testnet (default)
pyon-cli deploy SimpleStorage

# Deploy to mainnet
pyon-cli deploy SimpleStorage --network mainnet

# Deploy with constructor arguments
pyon-cli deploy SimpleStorage --args '[42]'

# Dry run (estimate gas only)
pyon-cli deploy SimpleStorage --dry-run
```

## 🐍 Python Smart Contracts

Pyon CLI allows you to write smart contracts in Python using a special syntax:

```python
from pyon_cli.py_contracts import PySmartContract

class SimpleStorage(PySmartContract):
    """Simple storage contract in Python."""
    
    def __init__(self):
        super().__init__()
        self.stored_data = self.state_var("stored_data", 0)
    
    @public_function
    def set(self, value: int):
        """Set stored data."""
        self.stored_data = value
        self.event("DataStored", value)
    
    @view_function
    def get(self) -> int:
        """Get stored data."""
        return self.stored_data
```

### Python Contract Features

- **State Variables**: Use `self.state_var(name, initial_value)`
- **Public Functions**: Use `@public_function` decorator
- **View Functions**: Use `@view_function` decorator
- **Events**: Use `self.event(name, *params)`
- **Basic Types**: Support for `int`, `str`, and basic operations

## 📋 CLI Commands

### Project Management

```bash
# Initialize project
pyon-cli init <project_name> [--force]

# Compile all contracts
pyon-cli compile [--contracts DIR] [--output DIR]
```

### Wallet Management

```bash
# Create new wallet
pyon-cli wallet new [--keystore FILE] [--password PASSWORD]

# Show wallet info
pyon-cli wallet show [--keystore FILE]
```

### Contract Deployment

```bash
# Deploy contract
pyon-cli deploy <contract_name> [OPTIONS]

# Options:
#   --args TEXT          Constructor arguments as JSON array
#   --config TEXT        Configuration file path
#   --dry-run           Estimate gas without deploying
#   --network TEXT      Override network (amoy/mainnet)
```

## ⚙️ Configuration

### Network Configuration (`pyon_config.json`)

```json
{
  "network": "amoy",
  "rpc_url": "https://rpc-amoy.polygon.technology",
  "chain_id": 80002,
  "explorer_api_key": ""
}
```

### Supported Networks

| Network | Chain ID | RPC URL |
|---------|----------|---------|
| Amoy (Testnet) | 80002 | https://rpc-amoy.polygon.technology |
| Mainnet | 137 | https://polygon-rpc.com |

## 🔐 Security

### Wallet Security

- Wallets are encrypted using PBKDF2 with SHA-256
- Private keys are never stored in plain text
- Support for environment variable (`PRIVATE_KEY`) for CI/CD

### Best Practices

1. **Never commit private keys** to version control
2. **Use strong passwords** for wallet encryption
3. **Backup your keystore files** securely
4. **Test on Amoy testnet** before mainnet deployment

## 📁 Project Structure

```
my-project/
├── contracts/           # Smart contracts (.sol and .py files)
│   ├── SimpleStorage.py
│   └── SimpleStorage.sol
├── build/              # Compiled contract artifacts
├── scripts/            # Deployment scripts
├── pyon_config.json    # Network configuration
├── pyon_key.json      # Encrypted wallet (created by CLI)
└── deployments.json   # Deployment history
```

## 🛠️ Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black pyon_cli/
isort pyon_cli/
```

### Type Checking

```bash
mypy pyon_cli/
```

## 📖 Examples

### Example 1: Counter Contract

```python
class Counter(PySmartContract):
    def __init__(self):
        super().__init__()
        self.count = self.state_var("count", 0)
    
    @public_function
    def increment(self):
        self.count = self.count + 1
        self.event("Incremented", self.count)
    
    @view_function
    def get_count(self) -> int:
        return self.count
```

### Example 2: Deployment Script

```python
#!/usr/bin/env python3
from pyon_cli.deployer import deploy_contract
from pyon_cli.wallet import WalletManager
import json

# Load configuration
with open("pyon_config.json") as f:
    config = json.load(f)

# Deploy contract
wallet = WalletManager()
result = deploy_contract(
    contract_name="Counter",
    constructor_args=[],
    config=config,
    wallet=wallet
)

print(f"Contract deployed at: {result['address']}")
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run the test suite
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/ShahiTechnovation/pyvax-cli/issues)
- **Documentation**: [GitHub README](https://github.com/ShahiTechnovation/pyvax-cli#readme)
- **Polygon Docs**: [Official Documentation](https://docs.polygon.technology/)

## 🔗 Links

- [Polygon Network](https://polygon.technology/)
- [Polygon Explorer](https://polygonscan.com/)
- [Amoy Testnet Faucet](https://faucet.polygon.technology/)

---

**⚡ Happy Building on Polygon! ⚡**