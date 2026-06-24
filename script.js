const firebaseConfig = {
  apiKey: "AIzaSyAAHcfBKTNNfUrDnAM8HO6wUelnv1liIog",
  authDomain: "ai-driven-dashboard-gene-88cad.firebaseapp.com",
  projectId: "ai-driven-dashboard-gene-88cad",
  storageBucket: "ai-driven-dashboard-gene-88cad.firebasestorage.app",
  messagingSenderId: "124976315338",
  appId: "1:124976315338:web:635bc837decab25acb6d33"
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const BACKEND_URL = 'http://localhost:5000';

let isRegister = false;

// UI Setup
document.addEventListener('DOMContentLoaded', () => {
    const toggleLink = document.getElementById('toggleLink');
    if (toggleLink) {
        toggleLink.onclick = (e) => {
            e.preventDefault();
            isRegister = !isRegister;
            document.getElementById('authButton').textContent = isRegister ? 'Register' : 'Login';
            document.getElementById('formTitle').textContent = isRegister ? 'Create Account' : 'Sign in to Dashboard';
        };
    }
});

// The Form Submission
const authForm = document.getElementById('authForm');
if (authForm) {
    authForm.onsubmit = async (e) => {
        e.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        try {
            console.log("Starting Auth...");
            if (isRegister) {
                // Step 1: Create User in Firebase
                await auth.createUserWithEmailAndPassword(email, password);
                alert("Account created successfully!");
            } else {
                // Step 1: Login to Firebase
                await auth.signInWithEmailAndPassword(email, password);
            }

            // Step 2: Try to notify Python (Don't let this block the redirect)
            saveStatsToPython(email);

            // Step 3: Go to Dashboard
            window.location.href = 'dashboard.html';

        } catch (error) {
            console.error("Auth Failed:", error.code);
            // This alert will tell you exactly what is wrong
            if (error.code === 'auth/email-already-in-use') alert("This email is already registered. Please Login.");
            else if (error.code === 'auth/weak-password') alert("Password must be at least 6 characters.");
            else if (error.code === 'auth/operation-not-allowed') alert("Go to Firebase Console -> Authentication -> Sign-in Method and ENABLE Email/Password.");
            else alert(error.message);
        }
    };
}

async function saveStatsToPython(email) {
    try {
        await fetch(`${BACKEND_URL}/api/stats`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                email: email,
                views: 60500, likes: 150, comments: 320, published: 70
            })
        });
    } catch (err) { console.log("Python offline, skipping stats sync."); }
}