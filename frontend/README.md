<!-- # React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...

      // Remove tseslint.configs.recommended and replace with this
      tseslint.configs.recommendedTypeChecked,
      // Alternatively, use this for stricter rules
      tseslint.configs.strictTypeChecked,
      // Optionally, add this for stylistic rules
      tseslint.configs.stylisticTypeChecked,

      // Other configs...
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])

```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])

``` -->
# 🚀 FinTrack

A modular investment portfolio management platform built with **FastAPI** and **React**.

FinTrack helps users manage digital assets, record transactions, track portfolio performance, and analyze investments through a modern dashboard.

---

# ✨ Features

## 💰 Asset Management

- ✅ Create new assets
- ✅ View all assets
- ✅ Delete assets
- ✅ Search assets by symbol

---

## 📊 Transaction Management

- ✅ Create BUY / SELL transactions
- ✅ Track transaction history
- ✅ Calculate transaction value
- ✅ Delete transactions
- ✅ Validate asset balance before selling

---

## 📈 Portfolio Tracking

- ✅ Calculate current holdings
- ✅ Calculate average buy price
- ✅ Track current portfolio value
- ✅ Calculate profit / loss

---

## 📉 Analytics Dashboard

- ✅ Total invested amount
- ✅ Current portfolio value
- ✅ Profit and loss calculation
- ✅ Profit percentage

---

# 🛠 Tech Stack

## Backend

- 🐍 Python
- ⚡ FastAPI
- 📦 Pydantic
- 🔄 Async API architecture
- 📁 JSON based persistence


## Frontend

- ⚛️ React
- ⚡ Vite
- 🟦 TypeScript
- 🎨 Tailwind CSS
- 🔄 React Query
- 🌐 Axios
- 🧭 React Router


---

# 📂 Project Structure
