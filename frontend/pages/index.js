import useSWR from 'swr'
import { useState } from 'react'

const fetcher = (url) => fetch(url).then(r => r.json())

export default function Home() {
  const [q, setQ] = useState('')
  const [resp, setResp] = useState(null)

  async function ask() {
    const res = await fetch(`/api/query?q=${encodeURIComponent(q)}`)
    const data = await res.json()
    setResp(data)
  }

  return (
    <main style={{ padding: 20 }}>
      <h1>RAG Study Buddy — PoC</h1>
      <input value={q} onChange={e => setQ(e.target.value)} placeholder="Ask a question" style={{ width: '60%' }} />
      <button onClick={ask} style={{ marginLeft: 8 }}>Ask</button>

      {resp && (
        <div style={{ marginTop: 20 }}>
          <h3>Answer</h3>
          <pre>{resp.answer}</pre>
          <h4>Sources</h4>
          <pre>{JSON.stringify(resp.sources, null, 2)}</pre>
        </div>
      )}
    </main>
  )
}
