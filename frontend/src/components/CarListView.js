import CarItem from './Car'

export default function CarView(props) {
    return (
        <div>
            <ul>
                {props.carList.map(car => <CarItem car={car} />)}
            </ul>
        </div>
    )
}