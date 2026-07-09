import type {
  ButtonHTMLAttributes,
} from "react";

interface ButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
}

function Button({
  children,
  ...props
}: ButtonProps) {
  return (
    <button
      {...props}
      className="
        bg-blue-600
        hover:bg-blue-700
        disabled:opacity-50
        disabled:cursor-not-allowed
        text-white
        px-4
        py-2
        rounded-lg
        transition
      "
    >
      {children}
    </button>
  );
}

export default Button;