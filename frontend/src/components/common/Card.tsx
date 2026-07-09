type CardProps = {
  children: React.ReactNode;
};

function Card({ children }: CardProps) {
  return (
    <div className="bg-white rounded-xl shadow p-5">
      {children}
    </div>
  );
}

export default Card;