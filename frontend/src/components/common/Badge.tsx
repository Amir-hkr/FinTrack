type BadgeProps = {
  text: string;
};

function Badge({ text }: BadgeProps) {
  return (
    <span className="bg-blue-100 text-blue-700 px-2 py-1 rounded text-sm">
      {text}
    </span>
  );
}

export default Badge;