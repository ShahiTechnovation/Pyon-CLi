# PyVax - Avalanche Smart Contract CLI

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**PyVax** is a production-ready CLI tool for deploying Solidity and Python smart contracts to Avalanche C-Chain. It features a unique **Python-to-EVM transpiler** that allows you to write smart contracts in Python and deploy them directly to the blockchain.

## 💡 What it does

PyVax is a powerful command-line interface that bridges the gap between Python developers and blockchain smart contract development. It enables developers to:

- Write smart contracts using familiar Python syntax
- Automatically transpile Python code to Solidity/EVM-compatible bytecode
- Deploy contracts to Avalanche C-Chain (Fuji testnet and mainnet)
- Manage wallets securely with encrypted keystores
- Interact with deployed contracts through an intuitive CLI
- Track deployment history and contract interactions

## 🎯 The problem it solves

Smart contract development has traditionally been limited to specialized languages like Solidity, creating a steep learning curve for developers. PyVax solves several critical problems:

- **High Barrier to Entry**: Traditional smart contract development requires learning Solidity, a specialized language with unique syntax and patterns
- **Limited Developer Accessibility**: Python developers, one of the largest programming communities, have been largely excluded from blockchain development
- **Complex Deployment Process**: Deploying contracts typically requires juggling multiple tools, manual ABI management, and complex configuration
- **Wallet Management Complexity**: Secure key management and wallet creation is often cumbersome and error-prone
- **Network Abstraction**: Switching between testnets and mainnet requires understanding RPC endpoints, chain IDs, and network configurations

By allowing developers to write smart contracts in Python and providing a unified CLI for the entire development lifecycle, PyVax dramatically lowers the barrier to blockchain development.

## 🚀 Features

- **Python Smart Contracts**: Write smart contracts in Python and transpile them to EVM bytecode
- **Solidity Support**: Full support for Solidity contract compilation and deployment
- **Multi-Network**: Deploy to Avalanche Fuji testnet or mainnet
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
python -m avax_cli.cli init my_project
cd my_project
```

This creates a new project with:
- Sample Python and Solidity contracts
- Default configuration file
- Deployment scripts

### 2. Create a Wallet

```bash
python -m avax_cli.cli wallet new
```

This will:
- Generate a new encrypted wallet
- Save it as `avax_key.json`
- Display your wallet address

**⚠️ Important**: Fund your wallet with AVAX before deploying contracts!

### 3. Compile Contracts

```bash
python -m avax_cli.cli compile
```

This compiles both Python and Solidity contracts in the `contracts/` directory.

### 4. Deploy Contracts

```bash
# Deploy to Fuji testnet (default)
python -m avax_cli.cli deploy SimpleStorage

# Deploy to mainnet
python -m avax_cli.cli deploy SimpleStorage --network mainnet

# Deploy with constructor arguments
python -m avax_cli.cli deploy SimpleStorage --args '[42]'

# Dry run (estimate gas only)
python -m avax_cli.cli deploy SimpleStorage --dry-run
```

## 🐍 Python Smart Contracts

PyVax allows you to write smart contracts in Python using a special syntax:

```python
from avax_cli.py_contracts import PySmartContract

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
# Initialize new project
avax-cli init <project_name> [--force]

# Compile contracts
avax-cli compile [--contracts contracts/] [--output build/]
```

### Wallet Management

```bash
# Create new wallet
avax-cli wallet new [--password PASSWORD] [--keystore avax_key.json]

# Show wallet info
avax-cli wallet show [--keystore avax_key.json]
```

### Contract Deployment

```bash
# Deploy contract
avax-cli deploy <contract_name> [OPTIONS]

# Options:
#   --args TEXT          Constructor arguments as JSON array
#   --config TEXT        Configuration file path
#   --dry-run           Estimate gas without deploying
#   --network TEXT      Override network (fuji/mainnet)
```

## ⚙️ Configuration

### Network Configuration (`avax_config.json`)

```json
{
  "network": "fuji",
  "rpc_url": "https://api.avax-test.network/ext/bc/C/rpc",
  "chain_id": 43113,
  "explorer_api_key": ""
}
```

### Supported Networks

| Network | Chain ID | RPC URL |
|---------|----------|---------|
| Fuji (Testnet) | 43113 | https://api.avax-test.network/ext/bc/C/rpc |
| Mainnet | 43114 | https://api.avax.network/ext/bc/C/rpc |

## 🔐 Security

### Wallet Security

- Wallets are encrypted using PBKDF2 with SHA-256
- Private keys are never stored in plain text
- Support for environment variable (`PRIVATE_KEY`) for CI/CD

### Best Practices

1. **Never commit private keys** to version control
2. **Use strong passwords** for wallet encryption
3. **Backup your keystore files** securely
4. **Test on Fuji testnet** before mainnet deployment

## 📁 Project Structure

```
my-project/
├── contracts/           # Smart contracts (.sol and .py files)
│   ├── SimpleStorage.py
│   └── SimpleStorage.sol
├── build/              # Compiled contract artifacts
├── scripts/            # Deployment scripts
│   └── deploy.py
├── avax_config.json    # Network configuration
└── deployments.json   # Deployment history
```

## 🛠️ Technologies I used

### Core Technologies
- **Python 3.8+**: Primary development language
- **Web3.py**: Ethereum/Avalanche blockchain interaction
- **Solc (py-solc-x)**: Solidity compiler integration
- **Click**: Command-line interface framework
- **Rich**: Beautiful terminal output and progress indicators
- **Cryptography**: PBKDF2 encryption for wallet security

### Blockchain Infrastructure
- **Avalanche C-Chain**: EVM-compatible blockchain platform
- **Fuji Testnet**: Development and testing environment
- **JSON-RPC**: Blockchain node communication protocol

### Development Tools
- **pytest**: Testing framework
- **black**: Code formatting
- **mypy**: Static type checking
- **setuptools**: Package distribution

## 🏗️ How we built it

PyVax was built through a systematic approach focusing on three core components:

### 1. Python-to-Solidity Transpiler
- Designed a custom Abstract Syntax Tree (AST) parser to analyze Python smart contract code
- Created mapping rules between Python syntax and Solidity equivalents
- Implemented state variable tracking, function decorators, and event emission translation
- Built type inference system to convert Python types to Solidity types

### 2. CLI Framework
- Developed modular command structure using Click framework
- Implemented wallet management with encrypted keystore support
- Created contract compilation pipeline supporting both .py and .sol files
- Built deployment orchestration with gas estimation and dry-run capabilities

### 3. Blockchain Integration
- Integrated Web3.py for Avalanche C-Chain communication
- Implemented multi-network support (Fuji/Mainnet) with configuration management
- Created transaction signing and broadcasting layer
- Built deployment tracking and contract interaction features

### Development Process
1. **Research Phase**: Studied Solidity semantics and Web3.py capabilities
2. **Prototype**: Built basic transpiler for simple contracts
3. **Iteration**: Enhanced transpiler to support complex DeFi patterns
4. **CLI Development**: Created user-friendly command interface
5. **Testing**: Extensive testing on Fuji testnet with various contract types
6. **Documentation**: Comprehensive guides and examples

## 🚧 Challenges I ran into

### 1. Type System Mismatch
**Challenge**: Python's dynamic typing vs Solidity's static typing  
**Solution**: Implemented type inference engine and required type hints for function parameters

### 2. State Management
**Challenge**: Translating Python's object-oriented state to Solidity's storage model  
**Solution**: Created special `state_var()` method to explicitly declare storage variables

### 3. Function Decorators
**Challenge**: Mapping Python decorators to Solidity function modifiers  
**Solution**: Developed custom decorator system (`@public_function`, `@view_function`) that translates to appropriate Solidity visibility

### 4. Gas Optimization
**Challenge**: Ensuring transpiled code is gas-efficient  
**Solution**: Implemented optimization passes in the transpiler and added dry-run mode for gas estimation

### 5. Wallet Security
**Challenge**: Balancing ease of use with secure key management  
**Solution**: Implemented encrypted keystore with PBKDF2 encryption and support for environment variables in CI/CD

### 6. Error Handling
**Challenge**: Providing meaningful error messages across compilation and deployment  
**Solution**: Created comprehensive error handling with rich formatting and actionable suggestions

## 📚 What we learned

### Technical Insights
- **Transpiler Design**: Deep understanding of AST manipulation and code generation
- **Blockchain Internals**: Detailed knowledge of EVM, gas mechanics, and transaction lifecycle
- **Security Best Practices**: Importance of proper key management and encryption standards
- **CLI UX Design**: How to create intuitive developer tools with clear feedback

### Development Lessons
- **Start Simple**: Beginning with basic contracts helped validate the core concept
- **Iterative Testing**: Continuous testing on testnet caught issues early
- **Documentation First**: Writing examples alongside code improved design decisions
- **Community Feedback**: Early user testing revealed UX improvements

### Blockchain Ecosystem
- **Avalanche Architecture**: Understanding of C-Chain's EVM compatibility and performance benefits
- **DeFi Patterns**: Common smart contract patterns in decentralized finance
- **Developer Pain Points**: What makes blockchain development challenging for newcomers

## 🛠️ Development

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black avax_cli/
isort avax_cli/
```

### Type Checking

```bash
mypy avax_cli/
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
from avax_cli.deployer import deploy_contract
from avax_cli.wallet import WalletManager
import json

# Load configuration
with open("avax_config.json") as f:
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

## 🚀 What's next for PyVax

### Short-term Goals
- **Enhanced Python Support**: 
  - Structs and custom types
  - Inheritance and composition patterns
  - Advanced error handling
- **Testing Framework**: Built-in unit testing for Python contracts
- **Interactive Debugger**: Step-through debugging for contracts
- **IDE Integration**: VS Code extension with syntax highlighting

### Medium-term Goals
- **Multi-chain Support**: 
  - Ethereum mainnet and testnets
  - Polygon
  - BSC (Binance Smart Chain)
  - Arbitrum and Optimism
- **Contract Templates**: Pre-built templates for common patterns (ERC-20, ERC-721, Governance)
- **Upgrade Management**: Support for upgradeable contracts and proxy patterns
- **Gas Optimization**: Advanced optimization passes in the transpiler

### Long-term Vision
- **Visual Contract Builder**: GUI tool for creating contracts without code
- **Contract Marketplace**: Share and discover community-built contracts
- **AI-Powered Assistant**: Smart suggestions and security analysis
- **Full DeFi Suite**: Built-in support for common DeFi protocols (DEXs, lending, staking)
- **Python Standard Library**: Comprehensive library of common contract patterns in Python

### Community & Ecosystem
- **Plugin System**: Allow community extensions and custom transpiler rules
- **Educational Resources**: Tutorials, workshops, and certification programs
- **Developer Community**: Forums, Discord, and collaborative development
- **Hackathon Support**: Sponsor and support blockchain hackathons

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

- **Issues**: [GitHub Issues](https://github.com/pyvax/avax-cli/issues)
- **Documentation**: [GitHub README](https://github.com/pyvax/avax-cli#readme)
- **Avalanche Docs**: [Official Documentation](https://docs.avax.network/)

## 🔗 Links

- [Avalanche Network](https://www.avax.network/)
- [Avalanche C-Chain Explorer](https://snowtrace.io/)
- [Fuji Testnet Faucet](https://faucet.avax.network/)

---

**⚡ Happy Building on Avalanche! ⚡**