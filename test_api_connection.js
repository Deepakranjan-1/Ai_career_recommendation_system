// Test API connection from frontend
const axios = require('axios');

const API_URL = 'https://ai-career-recommendation-system.onrender.com';

async function testAPI() {
    console.log('🧪 Testing API Connection');
    console.log('=' .repeat(40));
    
    try {
        // Test health endpoint
        console.log('1. Testing health endpoint...');
        const health = await axios.get(`${API_URL}/health`);
        console.log('✅ Health check passed');
        console.log(`   Status: ${health.data.status}`);
        
        // Test options endpoint
        console.log('\n2. Testing options endpoint...');
        const options = await axios.get(`${API_URL}/options`);
        console.log('✅ Options endpoint passed');
        console.log(`   Skills available: ${options.data.skills.length}`);
        console.log(`   Interests available: ${options.data.interests.length}`);
        
        // Test prediction endpoint
        console.log('\n3. Testing prediction endpoint...');
        const testData = {
            name: "Test User",
            age: 25,
            education: "Bachelor's",
            skills: ["Python", "Machine Learning"],
            interests: ["Technology", "Problem Solving"]
        };
        
        const prediction = await axios.post(`${API_URL}/predict`, testData);
        console.log('✅ Prediction endpoint passed');
        console.log(`   Predicted career: ${prediction.data.career}`);
        
        console.log('\n🎉 All API tests passed! Frontend can connect successfully.');
        
    } catch (error) {
        console.error('❌ API test failed:', error.message);
        if (error.response) {
            console.error('   Status:', error.response.status);
            console.error('   Data:', error.response.data);
        }
    }
}

testAPI();