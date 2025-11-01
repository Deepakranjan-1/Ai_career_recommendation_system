// API Configuration
export const API_CONFIG = {
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000',
  endpoints: {
    predict: '/predict',
    options: '/options',
    health: '/health'
  }
};

export const getApiUrl = (endpoint: string) => {
  return `${API_CONFIG.baseURL}${endpoint}`;
};