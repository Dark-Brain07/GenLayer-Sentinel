import { useState, useEffect } from 'react';
import { 
  Activity, Shield, Database, Cloud, DollarSign, 
  TrendingUp, BarChart3, Key, Lock, Network,
  RefreshCw, CheckCircle2, AlertTriangle
} from 'lucide-react';
import { createClient, createAccount, generatePrivateKey } from 'genlayer-js';
import { studionet } from 'genlayer-js/chains';

// Simulate GenLayer Connection
const account = createAccount(generatePrivateKey());
const client = createClient({
  chain: studionet,
  account: account,
});

// Mock Addresses for the 15 deployed contracts
const ORACLE_ADDRESSES = {
  weather: '0x9990000000000000000000000000000000001111',
  crypto: '0x9990000000000000000000000000000000002222',
  stock: '0x9990000000000000000000000000000000003333',
  social: '0x9990000000000000000000000000000000004444',
  github: '0x9990000000000000000000000000000000005555'
};

const SECURITY_ADDRESSES = {
  api_gateway: '0x8880000000000000000000000000000000001111',
  key_vault: '0x8880000000000000000000000000000000002222',
  rate_limiter: '0x8880000000000000000000000000000000003333',
  acl: '0x8880000000000000000000000000000000004444',
  multisig: '0x8880000000000000000000000000000000005555'
};

const LOGIC_ADDRESSES = {
  aggregator: '0x7770000000000000000000000000000000001111',
  subscription: '0x7770000000000000000000000000000000002222',
  archive: '0x7770000000000000000000000000000000003333',
  reputation: '0x7770000000000000000000000000000000004444',
  registry: '0x7770000000000000000000000000000000005555'
};

function StatusBadge({ status }) {
  return (
    <span className={`px-2 py-1 text-xs rounded-full font-medium ${
      status === 'active' ? 'bg-green-500/20 text-green-400 border border-green-500/30' :
      status === 'syncing' ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30' :
      'bg-red-500/20 text-red-400 border border-red-500/30'
    }`}>
      {status === 'active' && <span className="flex items-center gap-1"><CheckCircle2 className="w-3 h-3"/> Active</span>}
      {status === 'syncing' && <span className="flex items-center gap-1"><RefreshCw className="w-3 h-3 animate-spin"/> Syncing</span>}
      {status === 'error' && <span className="flex items-center gap-1"><AlertTriangle className="w-3 h-3"/> Error</span>}
    </span>
  );
}

function ContractCard({ title, address, icon: Icon, value, status }) {
  return (
    <div className="bg-surface-900 border border-slate-800 rounded-xl p-5 hover:border-brand-500/50 transition-colors">
      <div className="flex justify-between items-start mb-4">
        <div className="p-2 bg-brand-900/50 rounded-lg">
          <Icon className="w-5 h-5 text-brand-400" />
        </div>
        <StatusBadge status={status} />
      </div>
      <h3 className="text-slate-400 text-sm font-medium">{title}</h3>
      <p className="text-2xl font-bold mt-1 text-white">{value}</p>
      <div className="mt-4 pt-4 border-t border-slate-800/50 flex justify-between items-center">
        <span className="text-xs font-mono text-slate-500 truncate w-32">{address}</span>
        <a href={`https://explorer-studio.genlayer.com/address/${address}`} target="_blank" rel="noreferrer" className="text-xs text-brand-400 hover:text-brand-300">
          Explorer ↗
        </a>
      </div>
    </div>
  );
}

function App() {
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [data, setData] = useState({
    weather: '24°C, Clear',
    btc: '$64,230',
    aapl: '$178.45',
    sentiment: 'BULLISH',
    requests: '14,291',
    nodes: '12 Active'
  });

  const handleRefresh = () => {
    setIsRefreshing(true);
    // Simulate fetching new consensus data from GenLayer
    setTimeout(() => {
      setData(prev => ({
        ...prev,
        btc: '$' + (64000 + Math.floor(Math.random() * 1000)).toLocaleString(),
        requests: (parseInt(prev.requests.replace(',', '')) + Math.floor(Math.random() * 5)).toLocaleString()
      }));
      setIsRefreshing(false);
    }, 2000);
  };

  return (
    <div className="min-h-screen bg-surface-950 p-4 md:p-8 font-sans">
      
      {/* Header */}
      <header className="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center mb-10 gap-4">
        <div className="flex items-center gap-3">
          <div className="p-3 bg-brand-500 rounded-xl shadow-[0_0_20px_rgba(59,130,246,0.3)]">
            <Network className="w-6 h-6 text-white" />
          </div>
          <div>
            <h1 className="text-2xl font-bold bg-gradient-to-r from-white to-slate-400 bg-clip-text text-transparent">
              GenLayer Sentinel
            </h1>
            <p className="text-sm text-slate-500">Decentralized Oracle & Security Middleware</p>
          </div>
        </div>
        
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-2 px-4 py-2 bg-surface-900 border border-slate-800 rounded-lg text-sm text-slate-300">
            <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></div>
            Connected: StudioNet
          </div>
          <button 
            onClick={handleRefresh}
            disabled={isRefreshing}
            className="flex items-center gap-2 px-4 py-2 bg-brand-600 hover:bg-brand-500 disabled:opacity-50 text-white rounded-lg transition-all font-medium text-sm"
          >
            <RefreshCw className={`w-4 h-4 ${isRefreshing ? 'animate-spin' : ''}`} />
            Sync Oracles
          </button>
        </div>
      </header>

      <main className="max-w-7xl mx-auto space-y-12">
        
        {/* Layer 1: Data Oracles */}
        <section>
          <div className="flex items-center gap-2 mb-6 border-b border-slate-800 pb-2">
            <Database className="w-5 h-5 text-brand-400" />
            <h2 className="text-xl font-semibold text-slate-200">Layer 1: Data Oracles</h2>
            <span className="ml-2 px-2 py-0.5 bg-slate-800 text-slate-400 text-xs rounded-md">gl.nondet.exec_prompt</span>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <ContractCard title="Weather Feed" address={ORACLE_ADDRESSES.weather} icon={Cloud} value={data.weather} status="active" />
            <ContractCard title="Crypto Prices (BTC)" address={ORACLE_ADDRESSES.crypto} icon={DollarSign} value={data.btc} status={isRefreshing ? 'syncing' : 'active'} />
            <ContractCard title="Stock Market (AAPL)" address={ORACLE_ADDRESSES.stock} icon={TrendingUp} value={data.aapl} status="active" />
            <ContractCard title="Social Sentiment" address={ORACLE_ADDRESSES.social} icon={BarChart3} value={data.sentiment} status="active" />
          </div>
        </section>

        {/* Layer 2: Security */}
        <section>
          <div className="flex items-center gap-2 mb-6 border-b border-slate-800 pb-2">
            <Shield className="w-5 h-5 text-emerald-400" />
            <h2 className="text-xl font-semibold text-slate-200">Layer 2: Security & Privacy</h2>
            <span className="ml-2 px-2 py-0.5 bg-slate-800 text-slate-400 text-xs rounded-md">gl.eq_principle</span>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            <ContractCard title="API Gateway Proxy" address={SECURITY_ADDRESSES.api_gateway} icon={Network} value={data.requests} status={isRefreshing ? 'syncing' : 'active'} />
            <ContractCard title="Key Vault Controller" address={SECURITY_ADDRESSES.key_vault} icon={Key} value="Secured" status="active" />
            <ContractCard title="Access Control List" address={SECURITY_ADDRESSES.acl} icon={Lock} value="Enforced" status="active" />
            <ContractCard title="Multi-Sig Auth" address={SECURITY_ADDRESSES.multisig} icon={Shield} value="0 Pending" status="active" />
          </div>
        </section>

        {/* Layer 3: Utility */}
        <section>
          <div className="flex items-center gap-2 mb-6 border-b border-slate-800 pb-2">
            <Activity className="w-5 h-5 text-purple-400" />
            <h2 className="text-xl font-semibold text-slate-200">Layer 3: Utility & Logic</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="col-span-1 md:col-span-2 bg-surface-900 border border-slate-800 rounded-xl p-6">
              <h3 className="text-slate-400 text-sm font-medium mb-4">Master Registry Status</h3>
              <div className="space-y-4">
                <div className="flex justify-between items-center p-3 bg-surface-950 rounded-lg border border-slate-800/50">
                  <span className="text-sm text-slate-300">Total Services Indexed</span>
                  <span className="font-bold text-brand-400">15 / 15</span>
                </div>
                <div className="flex justify-between items-center p-3 bg-surface-950 rounded-lg border border-slate-800/50">
                  <span className="text-sm text-slate-300">Network Health AI Analysis</span>
                  <span className="px-2 py-1 bg-green-500/20 text-green-400 text-xs rounded-md border border-green-500/30">OPTIMAL</span>
                </div>
                <div className="flex justify-between items-center p-3 bg-surface-950 rounded-lg border border-slate-800/50">
                  <span className="text-sm text-slate-300">Oracle Reputation System</span>
                  <span className="font-bold text-white">{data.nodes}</span>
                </div>
              </div>
            </div>
            <div className="bg-gradient-to-br from-brand-900/50 to-surface-900 border border-brand-500/20 rounded-xl p-6 flex flex-col justify-center items-center text-center">
              <div className="p-4 bg-brand-500/20 rounded-full mb-4">
                <Database className="w-8 h-8 text-brand-400" />
              </div>
              <h3 className="text-lg font-bold text-white mb-2">Data Aggregator</h3>
              <p className="text-sm text-slate-400">Combining off-chain feeds into a single unified on-chain state via GenVM consensus.</p>
            </div>
          </div>
        </section>

      </main>
      
      <footer className="max-w-7xl mx-auto mt-20 pt-6 border-t border-slate-800 text-center text-sm text-slate-500">
        <p>GenLayer Sentinel Suite. Built for the GenLayer Developer Ecosystem.</p>
      </footer>
    </div>
  );
}

export default App;
