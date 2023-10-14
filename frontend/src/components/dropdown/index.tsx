import clsx from "clsx";
import React from "react";

interface Option {
  value: string;
  label: string;
}

interface DropdownProps {
  emptyOption: string;
  options: Option[];
  onChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
  value: string;
  className?: string;
}

const Dropdown = ({
  emptyOption,
  options,
  onChange,
  value,
  className,
}: DropdownProps) => {
  return (
    <>
      <select
        className={clsx(
          className,
          "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
        )}
        onChange={onChange}
        value={value}
      >
        <option defaultValue={""}>{emptyOption}</option>
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </>
  );
};

export default Dropdown;
