import { createBrowserRouter } from "react-router-dom";

import DashboardLayout from "../layouts/DashboardLayout";

import Dashboard from "../pages/Dashboard";
import Assets from "../pages/Assets";
import Portfolio from "../pages/Portfolio";
import Transactions from "../pages/Transactions";
import Analytics from "../pages/Analytics";
import Reports from "../pages/Reports";

const router = createBrowserRouter([
  {
    path: "/",
    element: <DashboardLayout />,
    children: [
      {
        index: true,
        element: <Dashboard />,
      },
      {
        path: "assets",
        element: <Assets />,
      },
      {
        path: "portfolio",
        element: <Portfolio />,
      },
      {
        path: "transactions",
        element: <Transactions />,
      },
      {
        path: "analytics",
        element: <Analytics />,
      },
      {
        path: "reports",
        element: <Reports />,
      },
    ],
  },
]);

export default router;