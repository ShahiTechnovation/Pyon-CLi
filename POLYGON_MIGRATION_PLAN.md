# 🔄 Avalanche to Polygon Migration Plan

## 📋 Executive Summary

This document outlines the comprehensive plan for migrating **Pyon CLI** from Avalanche blockchain to Polygon blockchain. This migration involves updating network configurations, changing gas token references, updating documentation, and modifying blockchain-specific code.

---

## 🎯 Migration Objectives

1. **Replace Avalanche network support with Polygon network**
2. **Update all blockchain-specific references (RPC URLs, Chain IDs, Gas tokens)**
3. **Maintain backward compatibility where possible**
4. **Update all documentation and user-facing content**
5. **Ensure seamless developer experience**

---

## 🔍 Key Differences: Avalanche vs Polygon

### Network Specifications

| Aspect | Avalanche | Polygon |
|--------|-----------|---------|
| **Mainnet Chain ID** | 43114 | 137 |
| **Testnet Chain ID** | 43113 (Fuji) | 80002 (Amoy) |
| **Gas Token** | AVAX | MATIC |
| **Testnet Name** | Fuji | Amoy (Mumbai deprecated) |
| **Mainnet RPC** | https://api.avax.network/ext/bc/C/rpc | https://polygon-rpc.com/ |
| **Testnet RPC** | https://api.avax-test.network/ext/bc/C/rpc | https://rpc-amoy.polygon.technology |
| **Mainnet Explorer** | https://snowtrace.io | https://polygonscan.com/ |
| **Testnet Explorer** | https://testnet.snowtrace.io | https://amoy.polygonscan.com |
| **Faucet** | https://faucet.avax.network | https://faucet.polygon.technology/ |
| **EVM Compatibility** | ✅ Yes (C-Chain) | ✅ Yes |
| **Consensus** | Snowman (PoS) | PoS (Bor + Heimdall) |
| **Block Time** | ~2 seconds | ~2 seconds |
| **TPS** | ~4,500 | ~7,000-65,000 |

### Technical Considerations

#### ✅ **What Stays the Same:**
- **EVM Compatibility**: Both are fully EVM-compatible
- **Smart Contract Languages**: Solidity contracts work unchanged
- **Web3.py Library**: Same library for blockchain interaction
- **Wallet Management**: Private key/keystore format identical
- **Contract ABIs**: No changes needed
- **Gas Estimation Logic**: Same methodology

#### ⚠️ **What Changes:**
- **Gas Token**: AVAX → MATIC
- **Network RPC Endpoints**: Different providers
- **Chain IDs**: Different numerical identifiers
- **Explorer URLs**: Snowtrace → Polygonscan
- **Network Names**: Fuji/Mainnet → Amoy/Polygon
- **Gas Costs**: Generally lower on Polygon (~0.001-0.01 MATIC vs 0.001-0.1 AVAX)
- **Transaction Speed**: Slightly faster on Polygon
- **Bridge Requirements**: Different cross-chain bridges

---

## 📂 Files Requiring Changes

### **Category 1: Critical Code Files** (Functional Changes)

#### 1.1 Configuration Files
- **`avax_config.json`**
  - Change RPC URLs
  - Update chain IDs
  - Change network names
  - **IMPACT**: High - Core configuration

#### 1.2 Core Python Modules
- **`avax_cli/utils.py`**
  - Update `get_network_info()` function
  - Change network configurations
  - Update token symbol references (AVAX → MATIC)
  - **IMPACT**: High - Network configuration logic

- **`avax_cli/deployer.py`**
  - Update comments referencing Avalanche
  - Change "AVAX" balance display to "MATIC"
  - Update connection logic comments
  - **IMPACT**: Medium - Display and logging

- **`avax_cli/cli.py`**
  - Update network override logic (fuji → amoy)
  - Change network names in commands
  - Update help text
  - Change "Deploy to Avalanche" → "Deploy to Polygon"
  - **IMPACT**: High - User-facing CLI

- **`avax_cli/interactor.py`**
  - Update network references in error messages
  - **IMPACT**: Low - Error messaging

- **`avax_cli/wallet.py`**
  - Update comments if Avalanche-specific
  - **IMPACT**: Low - Mostly network-agnostic

- **`avax_cli/shortcuts.py`**
  - Update environment check messages
  - Change project directory references
  - **IMPACT**: Low - Helper utilities

#### 1.3 Package Files
- **`pyproject.toml`**
  - Update description: "Avalanche C-Chain" → "Polygon"
  - Update keywords
  - **IMPACT**: Medium - Package metadata

- **`setup.py`**
  - Update description
  - Change package description
  - **IMPACT**: Medium - Package metadata

---

### **Category 2: Documentation Files**

#### 2.1 README Files
- **`README.md`**
  - Change title and descriptions
  - Update network configuration examples
  - Change "Avalanche" → "Polygon" throughout
  - Update RPC URLs and Chain IDs
  - Change "AVAX" → "MATIC"
  - Update explorer links
  - Update faucet links
  - **IMPACT**: High - Main documentation

- **`FINAL_README.md`**
  - Same changes as README.md
  - Update all network examples
  - Change command examples
  - Update deployment workflow
  - **IMPACT**: High - Comprehensive guide

- **`PYTHON_BEGINNER_GUIDE.md`**
  - Update blockchain references
  - Change network examples
  - Update "Avalanche" → "Polygon"
  - **IMPACT**: Medium - Educational content

- **`DEPLOYMENT_GUIDE.md`**
  - Update network information
  - Change deployed contract examples
  - Update explorer links
  - Change testnet references: Fuji → Amoy
  - **IMPACT**: High - Deployment instructions

#### 2.2 Configuration Examples
- **Example config files in project templates**
  - `my_project/avax_config.json`
  - `test_project/avax_config.json`
  - `nea/avax_config.json`
  - **IMPACT**: Medium - Template projects

#### 2.3 Script Templates
- **`examples/stake_token_examples.py`**
  - Update network references
  - **IMPACT**: Low - Example code

- **`my_project/scripts/deploy.py`**
- **`test_project/scripts/deploy.py`**
- **`nea/scripts/deploy.py`**
  - Update if Avalanche-specific
  - **IMPACT**: Low - Template scripts

---

### **Category 3: Branding & Naming** (Optional but Recommended)

#### 3.1 Module/Package Naming
- **Current**: `avax_cli` (Avalanche-specific)
- **Options**:
  1. Keep `avax_cli` (less confusion for existing users)
  2. Rename to `pyon_cli` (neutral, matches project name)
  3. Rename to `polygon_cli` (chain-specific)
- **RECOMMENDATION**: Rename to `pyon_cli` for future flexibility
- **IMPACT**: High - Breaking change requiring refactoring

#### 3.2 Configuration File Names
- **Current**: `avax_config.json`
- **Options**:
  1. Keep `avax_config.json` (legacy support)
  2. Rename to `pyon_config.json` (neutral)
  3. Rename to `polygon_config.json` (chain-specific)
- **RECOMMENDATION**: Rename to `pyon_config.json`
- **IMPACT**: Medium - User configuration

#### 3.3 Command Names
- **Current**: `avax-cli`
- **Options**:
  1. Keep `avax-cli`
  2. Change to `pyon-cli`
  3. Change to `polygon-cli`
- **RECOMMENDATION**: Change to `pyon-cli`
- **IMPACT**: High - User-facing command

---

## 🚨 Potential Consequences & Risks

### **Technical Risks**

#### 1. **Breaking Changes for Existing Users**
- **Risk**: Users with deployed contracts on Avalanche will lose access
- **Mitigation**: 
  - Provide multi-chain support instead of replacement
  - Add `--chain` flag to switch between networks
  - Maintain separate deployment files per chain

#### 2. **Gas Cost Differences**
- **Risk**: Gas estimation logic might be inaccurate
- **Mitigation**: 
  - Test gas estimation on Polygon testnet
  - Adjust gas buffer percentages if needed
  - Update documentation with Polygon-specific gas costs

#### 3. **RPC Provider Reliability**
- **Risk**: Different RPC providers have different reliability
- **Mitigation**:
  - Provide multiple RPC URL options
  - Add fallback RPC endpoints
  - Document rate limits

#### 4. **Module/Package Renaming**
- **Risk**: Breaking changes for users who imported `avax_cli`
- **Mitigation**:
  - Use deprecation warnings
  - Provide migration guide
  - Keep old imports working with compatibility layer

### **Business/User Experience Risks**

#### 1. **Brand Confusion**
- **Risk**: Project named "Pyon CLI" using `avax_cli` code
- **Impact**: Confusing for new users
- **Mitigation**: Complete rebrand to `pyon_cli`

#### 2. **Documentation Consistency**
- **Risk**: Mixed references to Avalanche and Polygon
- **Impact**: User confusion
- **Mitigation**: Thorough documentation review

#### 3. **Existing Deployments**
- **Risk**: Users lose ability to interact with Avalanche contracts
- **Impact**: Loss of functionality
- **Mitigation**: Multi-chain support or provide legacy branch

---

## 📋 Implementation Plan

### **Phase 1: Research & Planning** ✅ (Current Phase)
- [x] Analyze codebase for Avalanche-specific code
- [x] Identify all files requiring changes
- [x] Document Polygon network specifications
- [x] Create migration plan document
- [ ] Review with team/stakeholders

**Duration**: 1-2 days

---

### **Phase 2: Core Code Updates** (Critical Path)

#### Step 2.1: Update Network Configurations
**Files**: `avax_cli/utils.py`, `avax_config.json`

**Changes**:
```python
# Before (Avalanche)
"fuji": {
    "name": "Avalanche Fuji Testnet",
    "rpc_url": "https://api.avax-test.network/ext/bc/C/rpc",
    "chain_id": 43113,
    "explorer": "https://testnet.snowtrace.io",
    "faucet": "https://faucet.avax.network"
}

# After (Polygon)
"amoy": {
    "name": "Polygon Amoy Testnet",
    "rpc_url": "https://rpc-amoy.polygon.technology",
    "chain_id": 80002,
    "explorer": "https://amoy.polygonscan.com",
    "faucet": "https://faucet.polygon.technology"
}
```

**Tasks**:
- [ ] Update `get_network_info()` function
- [ ] Add Polygon mainnet configuration (Chain ID: 137)
- [ ] Add Polygon Amoy testnet configuration (Chain ID: 80002)
- [ ] Remove Avalanche configurations
- [ ] Update default network to "amoy"

**Duration**: 2 hours
**Priority**: 🔴 Critical

---

#### Step 2.2: Update CLI Commands
**Files**: `avax_cli/cli.py`

**Changes**:
- [ ] Replace "fuji" network option with "amoy"
- [ ] Update network override logic in `deploy()` command
- [ ] Change "Avalanche" → "Polygon" in help text
- [ ] Update "AVAX" → "MATIC" in balance displays
- [ ] Update success messages
- [ ] Update error messages

**Duration**: 3 hours
**Priority**: 🔴 Critical

---

#### Step 2.3: Update Deployer Module
**Files**: `avax_cli/deployer.py`

**Changes**:
- [ ] Update function docstrings (Avalanche → Polygon)
- [ ] Change balance display: "AVAX" → "MATIC"
- [ ] Update deployment cost messages
- [ ] Update connection comments
- [ ] Test gas estimation on Polygon

**Duration**: 2 hours
**Priority**: 🟡 High

---

#### Step 2.4: Update Project Initialization
**Files**: `avax_cli/cli.py` (init command)

**Changes**:
- [ ] Update default config template with Polygon settings
- [ ] Change example contract comments if needed
- [ ] Update generated README templates

**Duration**: 1 hour
**Priority**: 🟡 High

---

### **Phase 3: Configuration & Template Updates**

#### Step 3.1: Update Configuration Files
**Files**: All `*_config.json` files

**Changes**:
- [ ] `avax_config.json` → Update to Polygon
- [ ] `my_project/avax_config.json`
- [ ] `test_project/avax_config.json`
- [ ] `nea/avax_config.json`
- [ ] Consider renaming to `pyon_config.json`

**Duration**: 1 hour
**Priority**: 🟡 High

---

#### Step 3.2: Update Template Scripts
**Files**: `examples/`, `my_project/scripts/`, etc.

**Changes**:
- [ ] Update deployment scripts
- [ ] Change network references
- [ ] Update comments

**Duration**: 1 hour
**Priority**: 🟢 Medium

---

### **Phase 4: Documentation Updates**

#### Step 4.1: Update Main README
**File**: `README.md`

**Changes**:
- [ ] Change title/subtitle references
- [ ] Update network configuration section
- [ ] Change all "Avalanche" → "Polygon"
- [ ] Change all "AVAX" → "MATIC"
- [ ] Update RPC URLs and Chain IDs table
- [ ] Update explorer links
- [ ] Update faucet links
- [ ] Change "Fuji" → "Amoy"
- [ ] Update Quick Start section
- [ ] Update example commands

**Duration**: 2 hours
**Priority**: 🟡 High

---

#### Step 4.2: Update Comprehensive Guides
**Files**: `FINAL_README.md`, `PYTHON_BEGINNER_GUIDE.md`, `DEPLOYMENT_GUIDE.md`

**Changes**:
- [ ] Apply same changes as main README
- [ ] Update deployment examples
- [ ] Change network information sections
- [ ] Update live contract examples
- [ ] Update comparison tables

**Duration**: 3 hours
**Priority**: 🟡 High

---

#### Step 4.3: Update Package Metadata
**Files**: `pyproject.toml`, `setup.py`

**Changes**:
- [ ] Update description fields
- [ ] Change "Avalanche C-Chain" → "Polygon"
- [ ] Update keywords list
- [ ] Update project URLs if needed

**Duration**: 30 minutes
**Priority**: 🟢 Medium

---

### **Phase 5: Renaming & Refactoring** (Optional - Breaking Changes)

#### Step 5.1: Rename Module Package
**Current**: `avax_cli/` → **New**: `pyon_cli/`

**Changes**:
- [ ] Rename directory `avax_cli/` → `pyon_cli/`
- [ ] Update all imports across codebase
- [ ] Update `pyproject.toml` package name
- [ ] Update `setup.py` package name
- [ ] Update entry point: `avax-cli` → `pyon-cli`
- [ ] Add deprecation wrapper for old imports

**Duration**: 4 hours
**Priority**: 🟠 Optional (Recommended)

---

#### Step 5.2: Rename Configuration Files
**Current**: `avax_config.json` → **New**: `pyon_config.json`

**Changes**:
- [ ] Update file name references in code
- [ ] Add fallback support for old name
- [ ] Update documentation
- [ ] Add migration notice

**Duration**: 2 hours
**Priority**: 🟠 Optional (Recommended)

---

#### Step 5.3: Rename CLI Command
**Current**: `avax-cli` → **New**: `pyon-cli`

**Changes**:
- [ ] Update entry point in `pyproject.toml`
- [ ] Update entry point in `setup.py`
- [ ] Update all documentation
- [ ] Keep `avax-cli` as alias (deprecation)

**Duration**: 1 hour
**Priority**: 🟠 Optional (Recommended)

---

### **Phase 6: Testing & Validation**

#### Step 6.1: Functional Testing
- [ ] Test project initialization
- [ ] Test contract compilation (Solidity & Python)
- [ ] Test wallet creation
- [ ] Test connection to Polygon Amoy testnet
- [ ] Test contract deployment
- [ ] Test contract interaction (view functions)
- [ ] Test contract interaction (transactions)
- [ ] Test gas estimation
- [ ] Verify deployment tracking
- [ ] Test error handling

**Duration**: 4 hours
**Priority**: 🔴 Critical

---

#### Step 6.2: Integration Testing
- [ ] Test full deployment workflow on Amoy
- [ ] Deploy test contracts
- [ ] Verify on Polygonscan
- [ ] Test with real MATIC from faucet
- [ ] Test network switching
- [ ] Test multi-contract projects

**Duration**: 3 hours
**Priority**: 🔴 Critical

---

#### Step 6.3: Documentation Review
- [ ] Proofread all documentation
- [ ] Verify all links work
- [ ] Check for remaining Avalanche references
- [ ] Verify code examples work
- [ ] Update screenshots if any

**Duration**: 2 hours
**Priority**: 🟡 High

---

### **Phase 7: Deployment & Release**

#### Step 7.1: Version Management
- [ ] Decide version number (breaking change = major bump)
  - Current: 0.1.0 or 1.0.0
  - Recommended: 2.0.0 (major breaking change)
- [ ] Update version in `pyproject.toml`
- [ ] Update version in `setup.py`
- [ ] Create CHANGELOG.md

**Duration**: 1 hour
**Priority**: 🟡 High

---

#### Step 7.2: Repository Updates
- [ ] Update repository description on GitHub
- [ ] Update repository topics/tags
- [ ] Create migration guide for existing users
- [ ] Add migration notice to old README
- [ ] Consider creating a release branch for Avalanche version

**Duration**: 2 hours
**Priority**: 🟢 Medium

---

#### Step 7.3: Release Process
- [ ] Create Git tag for release
- [ ] Build package: `python -m build`
- [ ] Test installation: `pip install -e .`
- [ ] Publish to PyPI (if applicable)
- [ ] Create GitHub release with notes
- [ ] Announce changes to users

**Duration**: 2 hours
**Priority**: 🟡 High

---

## 📊 Estimated Timeline

### **Conservative Estimate** (with testing & review)
- **Phase 1**: Research & Planning - 2 days ✅
- **Phase 2**: Core Code Updates - 1 day
- **Phase 3**: Configuration Updates - 0.5 days
- **Phase 4**: Documentation - 1 day
- **Phase 5**: Renaming (Optional) - 1 day
- **Phase 6**: Testing - 1 day
- **Phase 7**: Release - 0.5 days

**Total**: ~7 days (without Phase 5) or ~8 days (with complete rebrand)

### **Aggressive Estimate** (experienced developer, minimal testing)
- **Phases 2-4**: 2-3 days
- **Phase 5**: 1 day
- **Phase 6**: 0.5 days
- **Phase 7**: 0.5 days

**Total**: ~4-5 days

---

## 🎯 Recommended Approach

### **Option A: Complete Migration (Recommended)**
**Pros**:
- Clean break from Avalanche
- Consistent branding (Pyon CLI + Polygon)
- No legacy code baggage
- Simpler codebase

**Cons**:
- Breaking changes for existing users
- Loses Avalanche support
- Requires version 2.0.0

### **Option B: Multi-Chain Support (Future-Proof)**
**Pros**:
- Supports both Avalanche and Polygon
- No breaking changes
- More valuable tool
- Can add more chains later

**Cons**:
- More complex implementation
- Larger codebase
- More testing required
- Need chain selection mechanism

**Implementation Approach for Option B**:
```python
# Add --chain flag
pyon-cli deploy MyContract --chain polygon
pyon-cli deploy MyContract --chain avalanche

# Or configure default in config
{
  "default_chain": "polygon",
  "chains": {
    "polygon": { ... },
    "avalanche": { ... }
  }
}
```

---

## 📝 Migration Checklist Summary

### **Must-Do Items** (Minimum Viable Migration)
- [ ] Update network configurations (RPC, Chain ID)
- [ ] Update CLI command network names
- [ ] Change gas token display (AVAX → MATIC)
- [ ] Update README.md
- [ ] Test on Polygon Amoy testnet
- [ ] Update package description

### **Should-Do Items** (Recommended)
- [ ] Rename `avax_cli` → `pyon_cli`
- [ ] Rename `avax_config.json` → `pyon_config.json`
- [ ] Rename `avax-cli` → `pyon-cli`
- [ ] Update all documentation files
- [ ] Update example projects
- [ ] Create migration guide

### **Nice-To-Have Items** (Optional)
- [ ] Multi-chain support
- [ ] Add Polygon zkEVM support
- [ ] Add chain comparison documentation
- [ ] Create demo video with Polygon
- [ ] Add Polygon-specific optimizations

---

## 🚀 Next Steps

1. **Review this plan** with team/stakeholders
2. **Decide on approach**: Complete migration vs Multi-chain
3. **Set timeline** and allocate resources
4. **Create backup** of current Avalanche version
5. **Begin Phase 2** implementation
6. **Regular testing** throughout implementation
7. **Communicate changes** to users before release

---

## 📞 Questions to Answer Before Implementation

1. **Do we want to maintain Avalanche support?**
   - If yes → Multi-chain approach
   - If no → Complete migration

2. **Should we rename the module to `pyon_cli`?**
   - Recommended: Yes, for consistency

3. **What version number for release?**
   - Recommended: 2.0.0 (breaking changes)

4. **Do we need to support users' existing deployments?**
   - If yes → Keep separate deployments.json per chain

5. **Should we keep a legacy Avalanche branch?**
   - Recommended: Yes, create `avalanche-legacy` branch

---

## 📚 Additional Resources

- **Polygon Documentation**: https://docs.polygon.technology/
- **Polygon RPC Endpoints**: https://wiki.polygon.technology/docs/pos/reference/rpc-endpoints/
- **Polygon Faucet**: https://faucet.polygon.technology/
- **Polygonscan**: https://polygonscan.com/
- **Amoy Testnet Explorer**: https://amoy.polygonscan.com
- **Polygon Gas Tracker**: https://polygonscan.com/gastracker

---

**Document Created**: 2024
**Last Updated**: 2024
**Status**: ✅ Ready for Review
**Priority**: 🔴 High Impact Migration
