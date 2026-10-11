import { useEffect, useState } from 'react'
import './App.css'

type Diagnostic = {
  summary: string
  recommendations: string[]
  gateway: {
    host: string
    reachable: boolean
    latency_ms?: number
    status: string
    details: string
  }
  internet: {
    host: string
    reachable: boolean
    latency_ms?: number
    status: string
    details: string
  }
  dns: {
    hostname: string
    reachable: boolean
    resolved_ips: string[]
    status: string
    details: string
  }
  latency: {
    average_ms?: number
    max_ms?: number
    min_ms?: number
    status: string
    target: string
  }
  stability: {
    status: string
    successful_checks: number
    failed_checks: number
    target: string
  }
}

const fallbackData: Diagnostic = {
  summary: '--',
  recommendations: ['--'],
  gateway: {
    host: '--',
    reachable: true,
    status: '--',
    details: '--',
  },
  internet: {
    host: '--',
    reachable: true,
    status: '--',
    details: '--',
  },
  dns: {
    hostname: '--',
    reachable: true,
    resolved_ips: ['--'],
    status: '--',
    details: '--',
  },
  latency: {
    status: '--',
    target: '--',
  },
  stability: {
    status: '--',
    successful_checks: 0,
    failed_checks: 0,
    target: '--',
  },
}

const apiBase = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000'

function App() {
  const [diagnostic, setDiagnostic] = useState<Diagnostic>(fallbackData)

  useEffect(() => {
    const controller = new AbortController()

    fetch(`${apiBase}/api/demo`, { signal: controller.signal })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Unable to fetch diagnostics')
        }
        return response.json() as Promise<Diagnostic>
      })
      .then((data) => {
        setDiagnostic(data)
      })
      .catch(() => undefined)

    return () => controller.abort()
  }, [])

  const statCards = [
    {
      label: 'Gateway',
      value: diagnostic.gateway.status === '--' ? '--' : diagnostic.gateway.reachable ? 'Reachable' : 'Offline',
      accent: diagnostic.gateway.reachable ? 'good' : 'bad',
    },
    {
      label: 'Internet',
      value: diagnostic.internet.status === '--' ? '--' : diagnostic.internet.reachable ? 'Connected' : 'Blocked',
      accent: diagnostic.internet.reachable ? 'good' : 'bad',
    },
    {
      label: 'DNS',
      value: diagnostic.dns.status === '--' ? '--' : diagnostic.dns.reachable ? 'Resolved' : 'Failed',
      accent: diagnostic.dns.reachable ? 'good' : 'bad',
    },
    {
      label: 'Latency',
      value: diagnostic.latency.average_ms
        ? `${diagnostic.latency.average_ms.toFixed(1)} ms`
        : '--',
      accent: diagnostic.latency.status === 'healthy' ? 'good' : 'warn',
    },
  ]

  return (
    <div className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">Wi‑Fi troubleshooting</p>
          <h1>NetPulse</h1>
        </div>
        <span className={`status-pill ${diagnostic.internet.status === '--' ? '' : diagnostic.internet.reachable ? 'online' : 'offline'}`}>
          {diagnostic.internet.status === '--' ? '--' : diagnostic.internet.reachable ? 'Network online' : 'Connectivity issue'}
        </span>
      </header>

      <main className="dashboard">
        <section className="summary-card">
          <div>
            <p className="section-label">Diagnostic summary</p>
            <h2>{diagnostic.summary}</h2>
          </div>
        </section>

        <section className="stats-grid">
          {statCards.map((card) => (
            <article key={card.label} className={`stat-card ${card.accent}`}>
              <span>{card.label}</span>
              <strong>{card.value}</strong>
            </article>
          ))}
        </section>

        <section className="panel-grid">
          <article className="panel">
            <h3>Gateway</h3>
            <p><strong>Host:</strong> {diagnostic.gateway.host}</p>
            <p><strong>Status:</strong> {diagnostic.gateway.status}</p>
            <p><strong>Latency:</strong> {diagnostic.gateway.latency_ms ?? '--'}{diagnostic.gateway.latency_ms ? ' ms' : ''}</p>
          </article>

          <article className="panel">
            <h3>Internet Reachability</h3>
            <p><strong>Target:</strong> {diagnostic.internet.host}</p>
            <p><strong>Status:</strong> {diagnostic.internet.status}</p>
            <p><strong>Latency:</strong> {diagnostic.internet.latency_ms ?? '--'}{diagnostic.internet.latency_ms ? ' ms' : ''}</p>
          </article>

          <article className="panel">
            <h3>DNS</h3>
            <p><strong>Hostname:</strong> {diagnostic.dns.hostname}</p>
            <p><strong>Status:</strong> {diagnostic.dns.status}</p>
            <p><strong>Resolved:</strong> {diagnostic.dns.resolved_ips.join(', ') || 'None'}</p>
          </article>

          <article className="panel">
            <h3>Stability</h3>
            <p><strong>Target:</strong> {diagnostic.stability.target}</p>
            <p><strong>Status:</strong> {diagnostic.stability.status}</p>
            <p><strong>Successful checks:</strong> {diagnostic.stability.successful_checks}</p>
            <p><strong>Failed checks:</strong> {diagnostic.stability.failed_checks}</p>
          </article>
        </section>

        <section className="panel recommendations">
          <h3>Recommended next steps</h3>
          <ul>
            {diagnostic.recommendations.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </section>
      </main>
    </div>
  )
}

export default App
