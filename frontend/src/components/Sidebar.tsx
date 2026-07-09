import { NavLink } from "react-router-dom";

const navItems = [
  { name: "Dashboard", path: "/" },
  { name: "Assets", path: "/assets" },
  { name: "Portfolio", path: "/portfolio" },
  { name: "Transactions", path: "/transactions" },
  { name: "Market", path: "/market" },
  { name: "Analytics", path: "/analytics" },
  { name: "Reports", path: "/reports" },
];

function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 text-white min-h-screen p-5 shadow-xl">
      <h1 className="text-3xl font-bold mb-10 text-center">
        FinTrack
      </h1>

      <nav className="flex flex-col gap-2">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            end={item.path === "/"}
            className={({ isActive }) =>
              `px-4 py-3 rounded-lg transition-all duration-200 font-medium ${
                isActive
                  ? "bg-blue-600 text-white shadow-md"
                  : "text-slate-300 hover:bg-slate-800 hover:text-white"
              }`
            }
          >
            {item.name}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}

export default Sidebar;