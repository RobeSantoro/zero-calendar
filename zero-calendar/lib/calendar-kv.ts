import { createClient } from "@vercel/kv"


const KV_REST_API_URL = "https://pet-scorpion-19203.upstash.io"
const KV_REST_API_TOKEN = "AUsDAAIjcDFiNzI1ZDEwMGU0YmM0NWIzYjlkNjgzN2RhOGU3YjQ2OXAxMA"


export const calendarKv = createClient({
  url: KV_REST_API_URL,
  token: KV_REST_API_TOKEN,
})
