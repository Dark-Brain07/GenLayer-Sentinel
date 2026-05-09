# GenLayer Sentinel - Comprehensive Deployment Guide

This guide covers the end-to-end deployment of the GenLayer Sentinel Infrastructure Suite, including all 15 Intelligent Contracts and the React Dashboard.

## Part 1: Contract Deployment (GenLayer Studio)

Due to the complex inter-dependencies of an infrastructure suite, the contracts must be deployed in specific phases using the [GenLayer Studio](https://studio.genlayer.com/).

### Prerequisites
1. Ensure your wallet (MetaMask/Rabby) is connected to the GenLayer testnet (StudioNet or Bradbury).
2. Ensure you have sufficient testnet GEN tokens to cover the deployment gas costs for 15 contracts.

### Deployment Phase 1: Security Core
*These contracts form the security middleware and should be deployed first so other contracts can reference them.*
1. Deploy `contracts/api_gateway_proxy.py`
2. Deploy `contracts/key_vault_controller.py`
3. Deploy `contracts/rate_limiter.py`
4. Deploy `contracts/access_control_list.py`
5. Deploy `contracts/multi_sig_authenticator.py`

### Deployment Phase 2: Data Oracles
*These are the core sensors that fetch external API data.*
6. Deploy `contracts/weather_oracle.py`
7. Deploy `contracts/crypto_price_feed.py`
8. Deploy `contracts/stock_market_oracle.py`
9. Deploy `contracts/social_sentiment_oracle.py`
10. Deploy `contracts/github_activity_oracle.py`

### Deployment Phase 3: Utility & Logic
*These contracts aggregate data and manage the ecosystem. They rely on the existence of the previous layers.*
11. Deploy `contracts/data_aggregator.py`
12. Deploy `contracts/subscription_manager.py`
13. Deploy `contracts/historical_archive.py`
14. Deploy `contracts/oracle_reputation.py`
15. Deploy `contracts/sentinel_registry.py`

### Post-Deployment Verification
After deploying each contract, copy its deployed address from the GenLayer Explorer. You must verify that the `gl.eq_principle` guards are functioning correctly by executing a test transaction (e.g., calling `update_weather("London")`) and ensuring the validators reach consensus.

---

## Part 2: Dashboard Deployment (Vercel)

The Sentinel monitoring dashboard is a React/Vite application that tracks the health of the 15 contracts.

### 1. Update Environment Configuration
Before deploying the dashboard, you must link it to your newly deployed contracts.
Open `dashboard/src/App.jsx` and locate the Address Constants at the top of the file:
```javascript
const ORACLE_ADDRESSES = { ... };
const SECURITY_ADDRESSES = { ... };
const LOGIC_ADDRESSES = { ... };
```
Replace the placeholder addresses (`0x999...`) with your actual deployed contract addresses from Part 1.

### 2. Local Testing
Verify the dashboard works locally with your contracts:
```bash
cd dashboard
npm install
npm run dev
```

### 3. Vercel Production Deployment
Deploy the dashboard to Vercel using the CLI:
```bash
# Login to your Vercel account
npx vercel login

# Deploy to production
npx vercel --prod
```

### 4. Custom Domain Routing (Optional)
To set up a custom, professional alias (e.g., `genlayersentinel.vercel.app`):
```bash
npx vercel alias [your-generated-vercel-url] genlayersentinel.vercel.app
```

---

## Part 3: Ongoing Maintenance

As a node operator for the Sentinel network, you should periodically call `analyze_network_health()` on the `sentinel_registry.py` contract to generate an AI-driven report on the network's capabilities and stability.
