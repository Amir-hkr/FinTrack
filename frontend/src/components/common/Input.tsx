type InputProps = {
  placeholder?: string;
};

function Input({ placeholder }: InputProps) {
  return (
    <input
      placeholder={placeholder}
      className="border rounded-lg px-3 py-2 w-full outline-none focus:ring-2 focus:ring-blue-500"
    />
  );
}

export default Input;