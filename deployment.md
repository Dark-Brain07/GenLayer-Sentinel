# Deployment Guide: GenLayer Sentinel

This document outlines the deployment strategy for the 15 Intelligent Contracts and the React Dashboard.

## 1. Contract Deployment
Because this is an infrastructure suite, contracts should be deployed in the following order using GenLayer Studio:

### Phase 1: Security Core
1. `api_gateway_proxy.py`
2. `key_vault_controller.py`
3. `rate_limiter.py`
4. `access_control_list.py`
5. `multi_sig_authenticator.py`

### Phase 2: Data Oracles
6. `weather_oracle.py`
7. `crypto_price_feed.py`
8. `stock_market_oracle.py`
9. `social_sentiment_oracle.py`
10. `github_activity_oracle.py`

### Phase 3: Logic & Utility
11. `data_aggregator.py`
12. `subscription_manager.py`
13. `historical_archive.py`
14. `oracle_reputation.py`
15. `sentinel_registry.py`

## 2. Dashboard Deployment (Vercel)

The infrastructure monitoring dashboard is designed to be hosted on Vercel.

```bash
cd dashboard
npm install
npm run build
vercel --prod
```

### Environment Variables
Update the `ORACLE_ADDRESSES`, `SECURITY_ADDRESSES`, and `LOGIC_ADDRESSES` constants in `src/App.jsx` with the actual deployed addresses from GenLayer Studio before deploying to production.
